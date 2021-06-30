/**
* This node js module handles search functionality.
*/

const gcs = require('@google-cloud/storage');
const NodeCache = require('node-cache'); //https://www.npmjs.com/package/node-cache#options
const csv = require('csvtojson');
const fs = require('fs');
const cloudconvert = new(require('cloudconvert'))('o99mxJrAzJpaUDhPL7JnViPik646Vdzu0xUoJM-XRVaJ5Y0iZOm3jvle2EXQPSBdOONWJpWbN_NSxdTOR0pMeA');
const parse = require('csv-parse');
const xlsx = require('node-xlsx');

// CORS Express middleware to enable CORS Requests.
const cors = require('cors')({
  origin: true,
});

// Import the queryProcessing.
const queryProcessing = require('./queryProcessing.js');
const quickSearchResponse = require('./quickSearchResponse.js');
const firestoreUtil = require('./firestoreUtil.js');
const arrayToJson = require('./arrayToJson.js');
const util = require('./util.js');
const gConst = require('./gConst');


// Import the Firebase SDK for Google Cloud Functions.
const functions = require('firebase-functions');
// Import and initialize the Firebase Admin SDK.
const admin = require('firebase-admin');
admin.initializeApp();

// Imports the Google Cloud client library
const {BigQuery} = require('@google-cloud/bigquery');

// The project ID to use, e.g. "your-project-id"
const projectId = "cloudstoragehelloworld";

// Instantiates a client
const bigquery = new BigQuery({
	projectId: projectId
});


const {Storage} = require('@google-cloud/storage');
const storage = new Storage({
	projectId: projectId
});

const firestoreDb = admin.firestore();

const nodemailer = require('nodemailer');
// Configure the email transport using the default SMTP transport and a GMail account.
// For Gmail, enable these:
// 1. https://www.google.com/settings/security/lesssecureapps
// 2. https://accounts.google.com/DisplayUnlockCaptcha
// For other types of transports such as Sendgrid see https://nodemailer.com/transports/
// TODO: Configure the `gmail.email` and `gmail.password` Google Cloud environment variables.
const gmailEmail = 'temp@email.com';//encodeURIComponent(functions.config().gmail.email);
const gmailPassword = 'psswrd';//encodeURIComponent(functions.config().gmail.password);
const mailTransport = nodemailer.createTransport(
	`smtps://${gmailEmail}:${gmailPassword}@smtp.gmail.com`);

function replyUserFn_(uid, queryMode, ts, botName, textMessage, searchResultTable, qsr, statsArray) {
	return replyUser_(uid, queryMode + '/fn', ts, botName, textMessage, searchResultTable, qsr, statsArray);
}

function replyUser_(uid, queryMode, ts, botName, textMessage, searchResultTable, qsr, statsArray) {
	var quickSearch = '';
	var stats = '';
	if (qsr) {
		quickSearch = qsr;
		stats = statsArray;
	}
	admin.database().ref('messages/' + uid).push({
		name: botName,
		queryMode: queryMode,
		timeStamp: ts,
		photoUrl: '/images/logo.png', // Firebase logo
		text: textMessage,
		botReply: 'true',
		searchResult: searchResultTable,
		quickSearch: quickSearch,
		stats: stats
	});
	return;
}

const memCacheUserLastResult = new NodeCache({
	stdTTL: 3600
});

function saveLastResult_(uid, queryMode, ts, searchResult, entityName, entityValue, columnName, hiddenColumnName) {
	var dataObj = {
		queryMode: queryMode,
		timeStamp: ts,
		searchResult: searchResult,
		entityName: entityName,
		entityValue: entityValue,
		columnName: columnName,
		hiddenColumnName: hiddenColumnName
	};

	memCacheUserLastResult.set(uid, dataObj);
	return admin.database().ref('LastResult/' + uid).push(dataObj);
}


// Async call to return result.
// callBackFn takes two arguments: 1. UID and 2. Last returned result.
function getLastResult(uid, callBackFn) {
	var value = memCacheUserLastResult.get(uid);
	if (value != undefined) {
		callBackFn(value);
		return;
	}
	console.log('key ' + uid + ' not found');

	// Reference to the /LastResult/ database path.
	var messagesRef = admin.database().ref('LastResult/' + uid);

	messagesRef.orderByKey().limitToLast(1).once("value", function(snapshot) {
		snapshot.forEach(function(data) {
			callBackFn(data.val());
			memCacheUserLastResult.set(uid, data.val()); // There was cache miss, then set it now.
			return true;
		});
	});
}


// replyQueryMessages reply to user message.
//exports.replyQueryMessages = functions.database.ref('/messages/{uid}/{messageId}').onCreate(
//  async(snapshot) => {
exports.replyQueryMessages = functions.database.ref('/messages/{uid}/{messageId}').onCreate(snapshot => {
	//const snapshot = event.data;
	// Only send a notification when a user message has been created.
//	if (snapshot.previous.val() || snapshot.val().botReply === 'true') {
	if (snapshot.val().botReply === 'true') {
		return;
	}

	const userMessage = snapshot.val().text;
	const uid = snapshot.val().uid;
	const ts = snapshot.val().timeStamp;
	console.log('New User Message:' + userMessage + ' With timeStamp:' + ts  + ' and UID is: ' + uid);
	

	const parsesUserRequest = queryProcessing.parseUserRequest(userMessage);
	const queryMode = parsesUserRequest.queryMode;
	switch (queryMode) {
		case 'help':
			return replyUserFn_(uid, queryMode, ts, 'Message from system', parsesUserRequest.userMessage, '');
		case 'quick-search':
			return quickSearchRespond(uid, queryMode, ts);
		case 'email':
			sendMailResponse(uid, queryMode, ts, parsesUserRequest.email);
			return;
		case 'btQuery':
			return queryAndSendBQResult(uid, queryMode, ts, parsesUserRequest);
		case 'hide':
			return changeColumnVisibility(uid, queryMode, ts, parsesUserRequest.columnNameArray, false);
		case 'show':
			return changeColumnVisibility(uid, queryMode, ts, parsesUserRequest.columnNameArray, true);
		case 'image':
			return replyUserFn_(uid, queryMode, ts, 'Message from system',
				'We are working on adding feature to show image of stone.', '');
		case 'video':
			return replyUserFn_(uid, queryMode, ts, 'Message from system',
				'We are working on adding feature to show video of stone.', '');
		case 'changeRate':
			return changeRateLastResult_(uid, queryMode, ts, parsesUserRequest.percent, parsesUserRequest.constUsd);
		case 'cache':
            firestoreUtil.FirestoreRead(uid, queryMode, ts, firestoreDb, replyUserFn_);
			return replyUserFn_(uid, queryMode, ts, 'Message from system',
				'Cache return', '');
		default:
			return replyUserFn_(uid, queryMode, ts, 'Message from system',
				'Your request is invalid, message/search "help" for usage instructions.', '');
	}
});

/*
 * https://github.com/firebase/functions-samples/blob/master/quickstarts/time-server/functions/index.js
 */
exports.loadData = functions.https.onRequest((req, res) => {
    if (req.method === 'PUT') {
    return res.status(403).send('Forbidden!');
  }
  
  // [START usingMiddleware]
  // Enable CORS using the `cors` express middleware.
  return cors(req, res, () => {
  	if (req.query) {
	  	console.log(" Req query:" + JSON.stringify(req.query));
  	}
  	console.log(" Req Json:" + JSON.stringify(req.method));

  	let companyCode = req.query.code; 
    console.log("loadData param: Company Code:" + companyCode);
    // [END readQueryParam]
    // Reading date format from request body query parameter
    console.log('Sending Company code back:' + companyCode);
    firestoreUtil.AddToFirestore(firestoreDb, req.body, companyCode);
    res.status(200).send("Response 200 from kp-Firebase" + companyCode);
    // [END sendResponse]
  });
});


const QuickSearchQuery =
	' SELECT ' +
	'  Color, ' +
	'  Clarity, ' +
	'  ROUND(Size,2) Carat, ' +
	'  FLOOR(Min(Rate_US)) Min_Price, ' +
	'  CEIL(Max(Rate_US)) Max_Price, ' +
	'  ROUND(Avg(Rate_US)) Avg_Price, ' +
	'  count(*) Count ' +
	' FROM cloudstoragehelloworld.Diamond_Inv.latest ' +
	' GROUP BY ' +
	'  Color, ' +
	'  Clarity, ' +
	'  Carat ' +
	' ORDER BY ' +
	'  Color, ' +
	'  Clarity, ' +
	'  Carat ';

const quickSearchMemCache = new NodeCache({
	stdTTL: 3600
});

// Using parsed user message (fully formed query), this function will query
// BQ and send the send to user.
// Query options list: https://cloud.google.com/bigquery/docs/reference/v2/jobs/query
function quickSearchRespond(uid, queryMode, ts) {
	var tempRows = quickSearchMemCache.get('quick-search');
	if (tempRows != undefined) {
		quickSearchReply(uid, queryMode, ts, tempRows);
		return;
	}
	// Given that query is generated correctly.
	const bqOptions = {
		query: QuickSearchQuery,
		useLegacySql: true // Use standard SQL syntax for queries.
	};

	console.log("Quick Search Query" + bqOptions.query);

	// Runs the query as a job
	// Link to sample code: https://cloud.google.com/bigquery/create-simple-app-api#bigquery-simple-app-query-nodejs
	bigquery
		.query(bqOptions)
		.then((results) => {
			const rows = results[0];
			quickSearchReply(uid, queryMode, ts, rows);
			memCache.set('quick-search', rows);
		}).catch((err) => {
			console.error('Quick Search BQ ERROR:', err);
		});
	replyUserFn_(uid, queryMode, ts, 'quick-search', 'We are working on your quick search request', '');
}

function quickSearchReply(uid, queryMode, ts, rows, cachedResult) {
	var qsr;
	if (cachedResult == null) {
		qsr = quickSearchResponse.createQuickSearchResponse(rows);
  		console.log('FireStore: Setting value in FireStore');
  		try {
			firestoreDb.collection('cache').doc('quick_search').set(JSON.stringify(qsr));
		} catch(error) {
			console.error('Firestore: Error setting document', error);
		}
	} else {
		qsr = cachedResult;
	}
	replyUser_(uid, queryMode, ts, 'Message from system', 'Click on any cell to search', '', qsr.quickSearchArray, qsr.stats);
}

/*
 * Using parsed user message (fully formed query), this function will query
 * BQ and send the send to user.
 *  Query options list: https://cloud.google.com/bigquery/docs/reference/v2/jobs/query
 */
function queryAndSendBQResult(uid, queryMode, ts, parsesUserRequest) {
	// Given that query is generated correctly.
	const bqOptions = {
		query: parsesUserRequest.query,
		useLegacySql: true // Use standard SQL syntax for queries.
	};

	var parsedQuery = parsesUserRequest.parsedQuery;

	var textReply = 'We are getting result for your search request: ' + parsesUserRequest.condition;

	// Runs the query as a job
	// Link to sample code: https://cloud.google.com/bigquery/create-simple-app-api#bigquery-simple-app-query-nodejs
	bigquery
		.query(bqOptions)
		.then((results) => {
			const rows = results[0];
			var resultArray = util.ParseBQResultAndCreateArray(rows, parsedQuery.columnName);
			replyUser_(uid, queryMode, ts, 'Search Result', 'Result is:', resultArray);
			saveLastResult_(uid, queryMode, ts, rows, parsedQuery.entityName, parsedQuery.entityValue,
				parsedQuery.columnName, parsedQuery.hiddenColumnName);
		}).catch((err) => {
			console.error('User Search BQ ERROR:', err);
		});
	replyUser_(uid, queryMode, ts, 'Search Result', textReply, '');
}


function changeColumnVisibility(uid, queryMode, ts, columnNameArray, showBool) {
	getLastResult(uid, function(lastResult) {
		var shownColumnName = lastResult.columnName;
		var newShownColumnName = [];
		var newHiddenColumnName = [];
		if (showBool) {
			newShownColumnName = shownColumnName;
			for (var i = 0; i < lastResult.hiddenColumnName.length; i++) {
				if (columnNameArray.indexOf(lastResult.hiddenColumnName[i]) != -1) {
					newShownColumnName.push(lastResult.hiddenColumnName[i]);
				} else {
					newHiddenColumnName.push(lastResult.hiddenColumnName[i]);
				}
			}
		} else {
			newHiddenColumnName = lastResult.hiddenColumnName;
			for (var i = 0; i < lastResult.columnName.length; i++) {
				if (columnNameArray.indexOf(lastResult.columnName[i]) != -1) {
					newHiddenColumnName.push(lastResult.columnName[i]);
				} else {
					newShownColumnName.push(lastResult.columnName[i]);
				}
			}
		}
		var resultArray = util.ParseBQResultAndCreateArray(lastResult.searchResult, newShownColumnName);
		replyUser_(uid, queryMode, ts, 'Search Result', 'Modified table is as follow:', resultArray);
		saveLastResult_(uid, queryMode, ts, lastResult.searchResult, lastResult.entityName, lastResult.entityValue,
			newShownColumnName, newHiddenColumnName);
	});
}

function changeRateLastResult_(uid, queryMode, ts, percent, constDollar) {
	getLastResult(uid, function(lastResult) {
		var changedRateData = util.ChangeRateUS(lastResult.searchResult, percent, constDollar);
		var resultArray = util.ParseBQResultAndCreateArray(changedRateData, lastResult.columnName);
		replyUser_(uid, queryMode, ts, 'Search Result', 'Modified table is as follow:', resultArray);
		saveLastResult_(uid, queryMode, ts, changedRateData, lastResult.entityName, lastResult.entityValue,
			lastResult.columnName, lastResult.hiddenColumnName);
	});
}

// TODO(DEVELOPER): Write the addWelcomeMessages Function here.
exports.addWelcomeMessages = functions.auth.user().onCreate(event => {
	const user = event.data;
	const fullName = user.displayName;
	console.log('A new user, ' + fullName + ', signed in for the first time.');

	// Sending notifications for new user to Admin.
	sendSearchResultEmail(fullName + ' signed in for the first time.', '', 'kalpesh@anikadiamond.com');

	// Saves the new welcome message into the database which then displays it in the user's screen
	admin.database().ref('messages/' + user.uid).push({
		name: 'Welcome Messenger',
		photoUrl: '/images/logo.png', // Firebase logo
		botReply: 'true',
		text: fullName + ' signed in for the first time! Welcome! \n' +
			'Type "help" to get started.'
	}).then(function() {
		admin.database().ref('users/' + user.uid).set({
			agreement: 0
		});
	});
});


// Sends a email to the given user.
// https://github.com/firebase/functions-samples/blob/master/quickstarts/email-users/functions/index.js
function sendSearchResultEmail(subject, resultTableData, toEmail) {
	const mailOptions = {
		from: 'Diamond Search <sales@anikadiamond.com>',
		to: toEmail
	};

	// The user subscribed to the newsletter.
	mailOptions.subject = subject;
	mailOptions.html = 'Hi,<br><br>Your report is as follow: <br><br>' +
		util.CreateHtmlTableFromResultArray(resultTableData) +
		'<br><br>Thanks for using Diamond Search.';

	return mailTransport.sendMail(mailOptions).then(() => {
		console.log('Search Result email sent to:' + toEmail);
	}).catch((err) => {
		console.error('Sending Email ERROR: ', err);
	});
}

function sendMailResponse(uid, queryMode, ts, toEmail) {
	var userReply = '';
	getLastResult(uid, function(lastResult) {
		if (lastResult.searchResult) {
			sendSearchResultEmail('Result from diamond search:',
				util.ParseBQResultAndCreateArray(lastResult.searchResult, lastResult.columnName),
				toEmail); //  Add back user query for result.
			userReply = 'Email was sent with following search Result';
		} else {
			userReply = 'No Results to send';
		}
		return replyUser_(uid, queryMode, ts, 'Email assistant', userReply, lastResult.searchResult);
	});
}

//Method for handling file upload
exports.eventForFile = functions.database.ref('/Inventory/{inventoryid}/file/').onWrite(event => {
	var snapshot = event.data;

	//When only status of the file changed from 1 to 2
	if (snapshot.previous.exists()) {
		return;
	}

	var inventoryId = snapshot.ref.parent.ref.key;
	var fileName = snapshot.val().filename;
	var statusOfFile = snapshot.val().status; //status for file wheather it is perfectly mapped or not
	var uid = snapshot.val().uid;

	var bucket = gcs.bucket("dinsightmessenger.appspot.com");
	var uploadedFile = bucket.file(uid + "/Personal/" + fileName); //complete file path of uploaded file
	var downloadUrl = "/tmp/" + fileName; //temporary download a file to this filepath for maniplation
	//different parse for .csv & .xls files, only two of them are allowed to upload
	if (fileName.split(".")[1] == "csv") {
		uploadedFile.download({
			destination: downloadUrl
		}).then(() => {
			//Simply read file using fs module
			fs.readFile(downloadUrl, function read(err, data) {
				if (err) {
					throw err;
				}
				try { // try block for errors during parsing, storing sample data & whole file data
					parse(data, {
						comment: '#'
					}, function(err, output) {
						//if parsed successfully then store extracted headers in database
						admin.database().ref("Inventory/" + inventoryId + "/ExtractedHeaders/").set({
							headers: output[0]
						}).then(function() {
							//Create sample data for displaying it in GUI and store it in database
							var i = 0;
							for (var j = 0; i < 4 && j < output.length; j++) {
								if (output[j].length == output[0].length) {
									admin.database().ref("Inventory/" + inventoryId + "/Sample/" + i + "/").set({
										row: output[j].join("|")
									});
									i++;
								}
							}
						}).then(function() {
							//if file was parsed successfully and sample data has been stored successfully then save message for user
							admin.database().ref("messages/" + uid).push({
								name: "System",
								text: fileName + " file parsed successfully",
								botReply: 'true',
								photoUrl: '/images/profile_placeholder.png'
							});
						}).then(function() {
							//Store file data in array form in database
							admin.database().ref("Inventory/" + inventoryId + "/Data/").set({
								data: output
							});
						});
					});
				} catch (error) {
					//if error occurs during parsing then save it for user
					admin.database().ref("messages/" + uid).push({
						name: "System",
						text: fileName + " file couldn't be parsed successfully",
						botReply: 'true',
						photoUrl: '/images/profile_placeholder.png'
					});
				}
			});
		});
	} else {
		uploadedFile.download({
			destination: downloadUrl
		}).then(() => {
			try { //try block for parsing file, storing sample data and storing whole data
				var obj = xlsx.parse(downloadUrl); // parses a file
				var rows = [];
				var writeStr = "";
				//looping through all sheets
				for (var i = 0; i < obj.length; i++) {
					var sheet = obj[i];
					//loop through all rows in the sheet
					for (var j = 0; j < sheet['data'].length; j++) {
						//add the row to the rows array
						rows.push(sheet['data'][j]);
					}
				}
				//if parsed successfully then store extracted headers in database
				admin.database().ref("Inventory/" + inventoryId + "/ExtractedHeaders/").set({
					headers: rows[0]
				}).then(function() {
					//Create sample data for displaying it in GUI and store it in database
					var i = 0;
					for (var j = 0; i < 4 && j < rows.length; j++) {
						if (rows[j].length == rows[0].length) {
							admin.database().ref("Inventory/" + inventoryId + "/Sample/" + i + "/").set({
								row: rows[j].join("|")
							});
							i++;
						}
					}
				}).then(function() {
					//if file was parsed successfully and sample data has been stored successfully then save message for user
					admin.database().ref("messages/" + uid).push({
						name: "System",
						text: fileName + " file parsed successfully",
						botReply: 'true',
						photoUrl: '/images/profile_placeholder.png'
					});
				}).then(function() {
					//Store file data in array form in database
					admin.database().ref("Inventory/" + inventoryId + "/Data/").set({
						data: rows
					});
				});
			} catch (error) {
				//if error occurs during parsing then save it for user
				admin.database().ref("messages/" + uid).push({
					name: "System",
					text: fileName + " file couldn't be parsed successfully",
					botReply: 'true',
					photoUrl: '/images/profile_placeholder.png'
				});
			}
		});
	}
});

//Testing methor for cloud convert
exports.eventForFile1 = functions.database.ref('/Inventory1/{uid}/file/').onWrite(event => {
	var snapshot = event.data;
	var fileName = snapshot.val().filename;
	var uid = snapshot.val().uid;
	var bucket = gcs.bucket("dinsightmessenger.appspot.com");
	var uploadedFile = bucket.file(uid + "/Personal/" + fileName);
	var downloadUrl = "/tmp/" + fileName;
	if (fileName.split(".")[1] == "csv") {
		uploadedFile.download({
			destination: downloadUrl
		}).then(() => {
			fs.readFile(downloadUrl, function read(err, data) {
				if (err) {
					throw err;
				}
				parse(data, {
					comment: '#'
				}, function(err, output) {
					writeStr = arrayToJson.arrayToJsonFn(output, "trial");
					admin.database().ref("Check/").push({
						text: "parsing done"
					});
					fs.writeFile("/tmp/test.txt", writeStr, function(err) {
						if (err) {
							return console.log(err);
						}
					});
					bucket.upload("/tmp/test.txt", {
						destination: "Edited/" + fileName.split(".")[0] + ".txt"
					});

				});
			});
		});
	} else {
		console.log("Starting of download" + fileName);
		uploadedFile.download({
			destination: downloadUrl
		}).then(() => {
			console.log("Completed download" + fileName);
			fs.createReadStream(downloadUrl)
				.pipe(cloudconvert.convert({
					"inputformat": "xls",
					"outputformat": "csv",
					"input": "upload"
				}))
				.pipe(fs.createWriteStream('/tmp/output.csv'));
		});
	}
});

//Method for parsing uploaded file and check if mapping is not correct or not
exports.eventForFileParsing = functions.database.ref('/Inventory/{inventoryid}/TemporaryExtractedArray/array').onWrite(event => {
	var snapshot = event.data;

	//project's default bucket
	var bucket = gcs.bucket("dinsightmessenger.appspot.com");

	//Mapping array uploaed by user
	var arrayOfIndex = snapshot.val();
	var loopLimit = arrayOfIndex.length;
	var companyIndex = [];
	//Convert string array to integer array
	for (var i = 0; i < loopLimit; i++) {
		companyIndex.push(parseInt(arrayOfIndex[i]));
	}

	var uid, companyCode;
	var inventoryId = snapshot.ref.parent.ref.parent.key;

	admin.database().ref("Inventory/" + inventoryId + "/file/").once('value', function(data) {
		uid = data.val().uid;
	}).then(function() {
		//Get uploaed filename first
		admin.database().ref("Inventory/" + inventoryId + "/file/").once('value', function(data) {
			lastFileName = data.val().companyname + getDateInFormat(); //New json formatted filename
			companyCode = data.val().code;
		}).then(function() {
			//Get stored file data from the database
			admin.database().ref("Inventory/" + inventoryId + "/Data/data").once('value', function(snapshot) {
				output = snapshot.val();
			}).then(function() {
				try { //try block for errors occured during validation of mapping
					writeStr = arrayToJson.arrayToJsonFn(output, companyIndex, companyCode);
					// TOODO(kalpesh): Upload the JSON to BigQuery
					try { //try block for errors occured during file upload and importane message saving
						fs.writeFile("/tmp/test.txt", writeStr, function(err) {
							if (err) {
								return console.log(err);
							}
						});
						//Clear previous error's value in database
						bucket.upload("/tmp/test.txt", {
							destination: "Edited/" + lastFileName + ".txt"
						}).then(function() {
							admin.database().ref("error/" + uid + "/").set({
								columnMapping: null
							});
							//Change inventory's status from 1 to 2
							admin.database().ref("Inventory/" + inventoryId + "/file/").update({
								status: "2"
							});
							//Save message for user that file parsed successfully
							admin.database().ref("messages/" + uid).push({
								name: "System",
								text: "Column mapping has been successfully done.",
								botReply: 'true',
								photoUrl: '/images/profile_placeholder.png'
							});
							//Save correct mapping array in database
							admin.database().ref("Inventory/" + inventoryId + "/ExtractedArray/").set({
								array: companyIndex
							});
						});
					} catch (err) {
						console.log(err.message); //show error on console log
						//Show error to user by saving it in error folder in database
						admin.database().ref("error/" + uid + "/").set({
							columnMapping: "Network error. Couldn't complete column mapping."
						});
						//Save error message for user in database
						admin.database().ref("messages/" + uid).push({
							name: "System",
							text: "Network error. Couldn't complete column mapping.",
							botReply: 'true',
							photoUrl: '/images/profile_placeholder.png'
						});
					}
				} catch (error) {
					console.log(error.message); //show error in console
					//Show error of columnn mis-matching by saving it in database
					admin.database().ref("error/" + uid + "/").set({
						columnMapping: error.message
					});
					//Save error message for user in database
					admin.database().ref("messages/" + uid).push({
						name: "System",
						botReply: 'true',
						text: error.message,
						photoUrl: '/images/profile_placeholder.png'
					});
				}
			});
		});
	});
});

//Method to notify system admin of registration of new company Administrator
exports.eventForAdminEntry = functions.database.ref('/users/{uid}/designation/').onWrite(event => {
	var snapshot = event.data;
	if (snapshot.val() == "Administrator") {
		//Save Administrator details under the request folder
		admin.database().ref("users/" + snapshot.ref.parent.key + "/").once('value', function(data) {
			admin.database().ref("Request/" + snapshot.ref.parent.key + "/").set({
				firstname: data.val().firstname,
				lastname: data.val().lastname,
				email: data.val().email,
				company: data.val().companyname
			});
		});
	}
});

//Method for removing enrty of admin registration after its approval
exports.eventForUserEntryApproval = functions.database.ref('/users/{uid}/approvalstatus/').onWrite(event => {
	var snapshot = event.data;
	var globalCompanyName = "";
	admin.database().ref("users/" + snapshot.ref.parent.key + "/").once('value', function(user) {
		globalCompanyName = user.val().companyname;
	}).then(function() {

		//do only if status changed to 1
		if (snapshot.val() == 1) {
			admin.database().ref("users/" + snapshot.ref.parent.key + "/").once('value', function(data) {
				//If admin't registration is approved
				if (data.val().designation == "Administrator") {
					//remove approval request from Request folder
					admin.database().ref("Request/" + snapshot.ref.parent.key + "/").set({
						firstname: null,
						lastname: null,
						email: null,
						company: null
					});
					//Add company name in the database
					admin.database().ref("Company/" + data.val().companyname + "/").set({
						companyname: data.val().companyname,
						permission: data.val().inventorypermission,
						admin: snapshot.ref.parent.key,
						code: data.val().code
					}).then(function() {
						//delete company code n inventory attrbute from user folder
						admin.database().ref("users/" + snapshot.ref.parent.key + "/").update({
							inventorypermission: null,
							code: null
						});
					});
				} else {
					//if employee's registration is approved then add its under the company's employee list
					var listOfEmployees = [];
					var companyName = data.val().companyname;
					if (companyName != "Other") {
						//get list of other employees for that company and store them in array
						admin.database().ref("Company/" + companyName + "/employees/").once('value', function(oldListOfEmployees) {
							oldListOfEmployees.forEach(function(grandchildnapshot) {
								listOfEmployees.push(grandchildnapshot.val());
							});
						}).then(function() {
							//Store new employee's id in that list
							listOfEmployees.push(snapshot.ref.parent.key);
							//remove duplicates
							var uniqueListOfEmployees = listOfEmployees.reduce(function(a, b) {
								if (a.indexOf(b) < 0) a.push(b);
								return a;
							}, []);
							//Store all employees list back under the company
							admin.database().ref("Company/" + companyName + "/").update({
								employees: uniqueListOfEmployees
							});
						});
					}
				}
			});
			//Assign permission for company's inventory
			var listOfCompanyId = [];
			//check for all companies permission
			admin.database().ref("Company").once('value', function(subsnapshot) {
				subsnapshot.forEach(function(subchildsnapshot) {
					if (subchildsnapshot.val().permission == "Public") {
						listOfCompanyId.push(subchildsnapshot.val().code);
					} else if (subchildsnapshot.val().permission == "Protected") {
						if (globalCompanyName == subchildsnapshot.key) {
							listOfCompanyId.push(subchildsnapshot.val().code);
						}
					} else {
						console.log("private");
					}
				});
			}).then(function() {
				admin.database().ref("UserAccessMapping/" + snapshot.ref.parent.key + "/").update({
					fileaccess: listOfCompanyId
				});
			});
		}
	});
});

exports.eventForFilePermission = functions.database.ref('/Company/{companyid}/permission/').onWrite(event => {
	//if deletion event
	if (!event.data.exists()) {
		return;
	}
	var userId, companyCode;
	var companyId = event.data.ref.parent.key;
	var permission = event.data;

	admin.database().ref("Company/" + companyId + "/").once('value', function(companycode) {
		companyCode = companycode;
	}).then(function() {
		if (event.data.previous.exists()) { //if permission is changed
			//Coding for permission change
		} else { //if permission is given first time
			if (permission.val() == "Public") {
				//if permission is public then assign company if to every employee of the database
				admin.database().ref("users/").once('value', function(snapshot) {
					snapshot.forEach(function(childsnapshot) {
						var accessString = [];
						//get al prrevious permission of the employee
						admin.database().ref("UserAccessMapping/" + childsnapshot.key + "/fileaccess/").once('value', function(oldAccessString) {
							oldAccessString.forEach(function(grandshildnapshot) {
								accessString.push(grandshildnapshot.val());
							});
							//add new permission
							accessString.push(companyCode);
						}).then(function() {
							//remove duplications
							var uniqueAccessString = accessString.reduce(function(a, b) {
								if (a.indexOf(b) < 0) a.push(b);
								return a;
							}, []);
							admin.database().ref("UserAccessMapping/" + childsnapshot.key + "/").update({
								fileaccess: uniqueAccessString
							});
						});
					});
				});
			} else if (permission.val() == "Protected") {

				admin.database().ref("users/").once('value', function(snapshot) {
					//if permission is protected then assign only to the same company's employee
					snapshot.forEach(function(childsnapshot) {
						if (childsnapshot.val().companyname == companyId) {
							var accessString = [];
							admin.database().ref("UserAccessMapping/" + childsnapshot.key + "/fileaccess/").once('value', function(oldAccessString) {
								oldAccessString.forEach(function(grandshildnapshot) {
									accessString.push(grandshildnapshot.val());
								});
								accessString.push(companyCode);
							}).then(function() {
								var uniqueAccessString = accessString.reduce(function(a, b) {
									if (a.indexOf(b) < 0) a.push(b);
									return a;
								}, []);
								admin.database().ref("UserAccessMapping/" + childsnapshot.key + "/").update({
									fileaccess: uniqueAccessString
								});
							});
						}
					});
				});

			} else {
				//Private function
				admin.database().ref("Company/" + companyId + "/").once('value', function(snapshot) {
					userId = snapshot.val().admin;
				}).then(function() {
					var accessString = [];
					admin.database().ref("UserAccessMapping/" + userId + "/fileaccess/").once('value', function(oldAccessString) {
						oldAccessString.forEach(function(grandshildnapshot) {
							accessString.push(grandshildnapshot.val());
						});
						accessString.push(companyCode);
					}).then(function() {
						var uniqueAccessString = accessString.reduce(function(a, b) {
							if (a.indexOf(b) < 0) a.push(b);
							return a;
						}, []);
						admin.database().ref("UserAccessMapping/" + userId + "/").update({
							fileaccess: uniqueAccessString
						});
					});
				});
			}
		}
	});
});

