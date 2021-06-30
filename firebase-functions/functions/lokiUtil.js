const gConst = require('./gConst');

exports.createSimpleQuery_ = function(whereClause, parsedQuery) {
	// parsedQuery //  (todo:kalpesh) change to add value to rate_us
	var rateMultiplier = 1.0 + (parsedQuery.percent) / 100;
	var limit = parsedQuery.limit;
	parsedQuery.columnName = gConst.columnNameC;
	parsedQuery.hiddenColumnName = gConst.hiddenColumnNameC;

	var btQueryStr =
		'SELECT ' +
		'Shape, ' +
		'Size,  ' +
		'Color, ' +
		'Clarity, ' +
		'Cut, ' +
		'Polish, ' +
		'Sym, ' +
		'Flour, ' +
		'ROUND(Rate_US*' + rateMultiplier + ') Rate_US, ' +
		'ROUND((Rate_US*' + rateMultiplier + ')/Size)  USDPerCT, ' +
		'SUBSTR(STRING(100 - ' + rateMultiplier + '*(100 - Back)),0, 5) Back, ' +
		'ReportNo, ' +
		'M1, ' +
		'M2, ' +
		'M3, ' +
		'Depth, ' +
		'[Table], ' + // https://stackoverflow.com/questions/18905842/oops-used-a-reserved-word-to-name-a-column
		'Ref, ' +
		'CertNo, ' +
		'Detail, ' +
		'cert, ' +
		'CompanyCode ' +
		'FROM Diamond_Inv.latest ' +
		' WHERE Rate_US != 0 AND ' +
		whereClause.join(' AND \n') +
		' ORDER BY USDPerCT ' +
		'LIMIT ' + limit;

	var btQuery = {
		query: btQueryStr
	};
	return btQuery;
}

//****************************************************************WHERE CLAUSE*****************************************


function testcreateWhereClause_(userMessage) {
	var whereClause = createWhereClause_(queryParser_(userMessage));
}

// createWhereClause_ create the big query from email query.
// parsedQuery is object with three fields.
// 1. userMessage (string query)
// 2. entityName array.
// 3. entityValue array. It is an 2D array.
exports.createWhereClause_ = function(parsedQuery) {

	var whereClause = [];
	var exactMode = false;
	if (parsedQuery.queryMode == 'exact') {
		exactMode = true;
	}

	for (var i = 0; i < parsedQuery.entityName.length; i++) {
		switch (parsedQuery.entityName[i]) {
			case 'color':
				var clause = getRangeClause_('color', parsedQuery.entityValue[i], gConst.colorRange, exactMode);
				whereClause.push(clause);
				break;
			case 'clarity':
				var clause = getRangeClause_('clarity', parsedQuery.entityValue[i], gConst.clarityRange, exactMode);
				whereClause.push(clause);
				break;
			case 'polish':
				var clause = getRangeClause_('polish', parsedQuery.entityValue[i], gConst.polishRange, exactMode);
				whereClause.push(clause);
				break;
			case 'sym':
				var clause = getRangeClause_('sym', parsedQuery.entityValue[i], gConst.symRange, exactMode);
				whereClause.push(clause);
				break;
			case 'cut':
				var clause = getRangeClause_('cut', parsedQuery.entityValue[i], gConst.cutRange, exactMode);
				whereClause.push(clause);
				break;
			case 'flour':
				var clause = getRangeClause_('flour', parsedQuery.entityValue[i], gConst.flourRange, exactMode);
				whereClause.push(clause);
				break;
			case 'size':
				var sizeClause = getSizeClause_(parsedQuery.entityValue[i]);
				whereClause.push(sizeClause);
				break;
			case 'shape':
				var shapeClause = getShapeClause_(parsedQuery.entityValue[i]);
				whereClause.push(shapeClause);
				break;
			case 'rate_us':
				var rateClause = getRateClause_(parsedQuery.entityValue[i]);
				whereClause.push(rateClause);
				break;
			case 'back':
				var BackClause = getBackClause_(parsedQuery.entityValue[i]);
				whereClause.push(BackClause);
				break;
			case 'reportno':
				var reportNoClause = getReportNoClause_(parsedQuery.entityValue[i]);
				whereClause.push(reportNoClause);
				break;
			default:
				// Nothing for now, but we should log it
		}
	}

	return whereClause;
}

// property examples are color, cut, clarity, etc
// valueArray = ['F', 'H']
// range = ['D', 'E', .... , 'Z']
function getRangeClause_(property, valueArray, range, exactMode) {
	var betterRange = -1;
	var lowerRange = -1;

	for (var j = 0; j < valueArray.length; j++) {
		for (var k = 0; k < range.length; k++) {
			if (valueArray[j] == range[k]) {
				if (betterRange == -1) {
					betterRange = k;
				} else {
					lowerRange = k;
				}
				break;
			}
		}
	}
	if (betterRange != -1) {
		retStr = [];
		if (lowerRange == -1) {
			if (exactMode) {
				retStr.push(property + ' = \'' + range[betterRange].toUpperCase() + '\'');
			} else {
				for (var k = 0; k <= betterRange; k++) {
					retStr.push(property + ' = \'' + range[k].toUpperCase() + '\'');
				}
			}
		} else {
			for (var k = betterRange; k <= lowerRange; k++) {
				retStr.push(property + ' = \'' + range[k].toUpperCase() + '\'');
			}
		}
		return "(" + retStr.join(' OR ') + ") ";
	}

	return '(true)';
}

function getShapeClause_(valueArray) {
	if (valueArray.length > 0) {
		var retStr = [];
		for (var i = 0; i < valueArray.length; i++) {
			var actualShape = getActualShape_(valueArray[i]);
			if (actualShape) {
				retStr.push('Shape = \'' + actualShape.toUpperCase() + '\'');
			}
		}
		return '(' + retStr.join(' OR ') + ')';
	}
	return '(true)';
}

function getReportNoClause_(valueArray) {
	if (valueArray.length > 0) {
		var retStr = [];
		for (var i = 0; i < valueArray.length; i++) {
			retStr.push('reportno = \'' + valueArray[i] + '\'');
		}
		return '(' + retStr.join(' OR ') + ')';
	}
	return '(true)';
}

// Add keyword like quater, 3rd's, halfs,
function getSizeClause_(valueArray) {
	var firstSize = -1.0;
	var secondSize = -1.0;

	for (var j = 0; j < valueArray.length; j++) {
		if (validDecimal_(valueArray[j])) {
			if (firstSize < 0.0) {
				firstSize = valueArray[j];
			} else {
				secondSize = valueArray[j];
			}
		}
	}
	if (firstSize > 0.0) { //First value is initialize
		if (secondSize < 0.0) { // If second value is not initialize then it should single value.
			return '(Size = ' + firstSize + ')';
		} else { // If both values are initialize then it range.
			if (firstSize > secondSize) {
				return '( Size < ' + firstSize + ' AND size > ' + secondSize + ')';
			} else {
				return ' (Size < ' + secondSize + ' AND size > ' + firstSize + ')';
			}
		}
	}
	return null;
}

// For keyword like ['price','prise','value','cost','dollar','rate','$','dollar',]
function getRateClause_(valueArray) {
	if (valueArray.length == 1) {
		return '(Rate_US <= ' + valueArray[0] + ')';
	} else if (valueArray.length == 2) {
		var firstSize = valueArray[0];
		var secondSize = valueArray[1];
		if (firstSize > secondSize) {
			return '(Rate_US <= ' + firstSize + ' AND Rate_US >= ' + secondSize + ')';
		} else {
			return '(Rate_US <= ' + secondSize + ' AND Rate_US >= ' + firstSize + ')';
		}
	} else {
		return '(true)';
	}
}

// backTypo: ['back','discount','off','%',]
function getBackClause_(valueArray) {
	var firstSize = -1.0;
	var secondSize = -1.0;
	for (var j = 0; j < valueArray.length; j++) {
		if (validDecimal_(valueArray[j])) {
			if (firstSize < 0.0) {
				firstSize = valueArray[j];
			} else {
				secondSize = valueArray[j];
			}
		}
	}
	if (firstSize > 0.0) { //First value is initialize
		if (secondSize < 0.0) { // If second value is not initialize then it should single value.
			return '(Back > ABS(' + firstSize + '))';
		} else { // If both values are initialize then it range.
			if (firstSize > secondSize) {
				return '(Back < ABS(' + firstSize + ') AND Back > ABS(' + secondSize + '))';
			} else {
				return '(Back < ABS(' + secondSize + ') AND Back > ABS(' + firstSize + '))';
			}
		}
	}
	return null;
}

function validDecimal_(value) {
	return !isNaN(parseFloat(value));
}



// Using parsed user message (fully formed query), this function will query
// BQ and send the send to user.
// Query options list: https://cloud.google.com/bigquery/docs/reference/v2/jobs/query
function lokiTest(uid, queryMode, ts) {
	// var db = new loki('invdb.json');
	//
	// // Link to sample code: https://cloud.google.com/bigquery/create-simple-app-api#bigquery-simple-app-query-nodejs
	// // var lokiRows = diamonds.find({Shape: 'ROUND'});
	// if (db.getCollection('diamonds')) {
	//   var diamonds = db.getCollection('diamonds'); //add index to improve performance.
	//   lokiTestQuery(uid, queryMode, ts, diamonds);
	//   //   var resultArray = parseBQResultAndCreateArray_(lokiRows, shownColumnName);
	//   //   replyUser_(uid, queryMode, ts, 'lokiTestQuery', 'Loki Search Result is count is:' + lokiRows.length, resultArray);
	// } else {
	//   var diamonds = db.addCollection('diamonds'); //add index to improve performance.
	//
	//   replyUser_(uid, queryMode, ts, 'loki-db', 'We are working on your fastest search engine: ', '');
	//
	//   // Writing to Google storage
	//   writeToGoogleStorage(0, db);
	// }
}

const companyNameList = ['Dharam']; //, 'Kiran', 'RK'];

function writeToGoogleStorage(companyIndex, db) {
	if (companyIndex >= companyNameList.length) {
		loadLokiFromStorage(0, db);
		return;
	}

	var companyName = companyNameList[companyIndex];
	let job;
	// Exports data from the table into a Google Cloud Storage file
	// https://cloud.google.com/bigquery/docs/exporting-data#bigquery-export-table-gcs-nodejs
	bigquery
		.dataset(companyName + '_Inv')
		.table('latest')
		.export(storage.bucket('dinsightinventory').file(companyName + '_inventory'))
		.then((results) => {
			job = results[0];
			console.log(`${companyName} Job ${job.id} started.`);
			return job.promise();
		})
		.then((results) => {
			console.log(`${companyName} Job ${job.id} completed.`);
			writeToGoogleStorage(companyIndex + 1, db);
		})
		.catch((err) => {
			console.error(companyName + '  ERROR:', err);
		});
}

function loadLokiFromStorage(companyIndex, db) {
	if (companyIndex >= companyNameList.length) {
		db.saveDatabase();
		return;
	}
	var diamondCollection = db.getCollection('diamonds');
	var companyName = companyNameList[companyIndex];
	console.log('loadLokiFromStorage: for' + companyName);
	const blob = storage
		.bucket('dinsightinventory')
		.file(companyName + '_inventory');
	var blobReadStream = blob.createReadStream(); // https://cloud.google.com/appengine/docs/flexible/nodejs/using-cloud-storage
	console.log('PT1: for' + companyName);

	//https://www.npmjs.com/package/csvtojson  other useful link: https://www.npmjs.com/package/git-blob-stream
	csv()
		.fromStream(blobReadStream) //
		.on('json', function(jsonObj) {
			//      console.log('PT2: jsonObj' + JSON.stringify(jsonObj));
			diamondCollection.insert(jsonObj);
		})
		.on('done', function() {
			console.log('PT3: for' + companyName);
			//parsing finished
			loadLokiFromStorage(companyIndex + 1, db);

		});
	// .on('done',(error)=>{
	//   console.log('PT3: for' + companyName + ' end error:' + error);
	//   loadLokiFromStorage(companyIndex + 1);
	//   db.saveDatabase();
	// })

	console.log('PT4: for' + companyName);
}

function lokiTestLoad(uid, queryMode, ts, rows) {
	// rows = parseRows_(rows);
	// diamonds.insert(rows);
	// replyUser_(uid, queryMode, ts, 'loki-db', 'loki-db: Loading data complete', '');
	// console.log("lokiTestLoad with row count:" + rows.length);
}

function parseRows_(rows) {
	var retRows = [];
	rows.forEach((row) => {
		//console.log("parseRows_ JSON:" + JSON.stringify(row));
		var valuesStr = row['val'];
		if (valuesStr != undefined) {
			var values = valuesStr.split("#");
			if (values.length == 21) {
				var retRow = {
					Shape: values[0],
					Size: values[1],
					Color: values[2],
					Clarity: values[3],
					Cut: values[4],
					Polish: values[5],
					Sym: values[6],
					Flour: values[7],
					Rate_US: values[8],
					Back: values[9],
					ReportNo: values[10],
					M1: values[11],
					M2: values[12],
					M3: values[13],
					Depth: values[14],
					Table: values[15],
					Ref: values[16],
					CertNo: values[17],
					Detail: values[18],
					cert: values[19],
					CompanyCode: values[20]
				};
				retRows.push(retRow);
			}
		}
	});
	return retRows;
}

function addTask(description) {
	//
	// var docRef = firestoreDb.collection('users').doc('alovelace');
	//
	// var setAda = docRef.set({
	//     first: 'Ada',
	//     last: 'Lovelace',
	//     born: 1815
	// });


	// const taskKey = datastore.key('Task');
	// const entity = {
	//   key: taskKey,
	//   data: [
	//     {
	//       name: 'created',
	//       value: new Date().toJSON()
	//     },
	//     {
	//       name: 'description',
	//       value: description,
	//       excludeFromIndexes: true
	//     },
	//     {
	//       name: 'done',
	//       value: false
	//     }
	//   ]
	// };
	//
	// datastore.save(entity)
	// .then(() => {
	//   console.log(`Task ${taskKey.id} created successfully.`);
	//   listTasks();
	// })
	// .catch((err) => {
	//   console.error('ERROR:', err);
	// });
}

function listTasks() {
	// const query = datastore.createQuery('Task')
	// .order('created');
	//
	// datastore.runQuery(query)
	// .then((results) => {
	//   const tasks = results[0];
	//
	//   console.log('Tasks:');
	//   tasks.forEach((task) => {
	//     const taskKey = task[datastore.KEY];
	//     console.log(taskKey.id, task);
	//   });
	// })
	// .catch((err) => {
	//   console.error('ERROR:', err);
	// });
}
