/**
 * Created by kalpesh on 5/22/17.
 */

//Used for spanner but should be similar for BigQuery.
// From https://cloud.google.com/functions/docs/tutorials/use-cloud-spanner

// for BQ, link to tutorial is https://cloud.google.com/bigquery/create-simple-app-api#bigquery-simple-app-query-nodejs
// https://cloud.google.com/bigquery/docs/tables#bigquery-list-tables-nodejs

//  Outside example with different bigQuery options like query, delete, etc.
// https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/bigquery/tables.js

// Other example of BigQuery table example is
// https://gist.github.com/soundTricker/2917197


//
// // Imports the Google Cloud client library
// const Spanner = require('@google-cloud/spanner');
//
// // Instantiates a client
// const spanner = Spanner();
//
// // Your Cloud Spanner instance ID
// const instanceId = 'test-instance';
//
// // Your Cloud Spanner database ID
// const databaseId = 'example-db';
//
// /**
//  * HTTP Cloud Function.
//  *
//  * @param {Object} req Cloud Function request context.
//  * @param {Object} res Cloud Function response context.
//  */
// exports.get = (req, res) => {
//     // Gets a reference to a Cloud Spanner instance and database
//     const instance = spanner.instance(instanceId);
//     const database = instance.database(databaseId);
//
//     // The query to execute
//     const query = {
//         sql: 'SELECT * FROM Albums'
//     };
//
//     // Execute the query
//     return database.run(query)
//             .then((results) => {
//             const rows = results[0].map((row) => row.toJSON());
//     rows.forEach((row) => {
//         res.write(`SingerId: ${row.SingerId.value}, AlbumId: ${row.AlbumId.value}, AlbumTitle: ${row.AlbumTitle}\n`);
// });
//     res
//         .status(200)
//         .end();
// })
// .catch((err) => {
//         res
//         .status(500)
//         .send(`Error querying Spanner: ${err}`)
//         .end();
// });
// };


CREATE TEMPORARY FUNCTION colorcategory(str STRING)
RETURNS STRING
LANGUAGE js AS ""
"
if (str == 'D' || str == 'E' || str == 'F') {
	return 'D';
}
if (str == 'G' || str == 'H') {
	return 'G';
}
if (str == 'I' || str == 'J') {
	return 'I';
}
if (str == 'K' || str == 'L' || str == 'M' || str == 'N') {
	return 'K';
}
""
";

SELECT
ColorCategory(Color) Color,
	Clarity,
	ROUND(Size, 1) Carat,
	ROUND(Min(Rate_US)) Min_Price,
	ROUND(Max(Rate_US)) Max_Price,
	ROUND(Avg(Rate_US)) Avg_Price,
	count( * ) Count
FROM cloudstoragehelloworld.Kiran_Inv.latest
Group by
Color,
Clarity,
Carat
Order By
Avg_Price Desc



SELECT
Color,
Clarity,
ROUND(Size, 2) Carat,
	ROUND(Min(Rate_US)) Min_Price,
	ROUND(Max(Rate_US)) Max_Price,
	ROUND(Avg(Rate_US)) Avg_Price,
	count( * ) Count
FROM cloudstoragehelloworld.Diamond_Inv.latest
Group by
Color,
Clarity,
Carat
Order By
Color,
Clarity,
Carat


// Sends a notifications to all users when a new message is posted.
// exports.sendNotifications = functions.database.ref('/messages/{uid}/{messageId}').onWrite(event => {
//     const snapshot = event.data;
//     // Only send a notification when a message has been created.
//     if (snapshot.previous.val()) {
//         return;
//     }
//
//     // Notification details.
//     const text = snapshot.val().text;
//     const uid = snapshot.val().uid;
//     const payload = {
//         notification: {
//             title: `${snapshot.val().name} posted ${text ? 'a message' : 'an image'}`,
//             body: text ? (text.length <= 100 ? text : text.substring(0, 97) + '...') : '',
//             icon: snapshot.val().photoUrl || '/images/profile_placeholder.png',
//             click_action: `https://${functions.config().firebase.authDomain}`
//         }
//     };
//
//     // Get the list of device tokens.
//     return admin.database().ref('fcmTokens/' + uid).once('value').then(allTokens => {
//             if (allTokens.val()) {
//         // Listing all tokens.
//         const tokens = Object.keys(allTokens.val());
//
//         // Send notifications to all tokens.
//         return admin.messaging().sendToDevice(tokens, payload).then(response => {
//                 // For each message check if there was an error.
//                 const tokensToRemove = [];
//         response.results.forEach((result, index) => {
//             const error = result.error;
//         if (error) {
//             console.error('Failure sending notification to', tokens[index], error);
//             // Cleanup the tokens who are not registered anymore.
//             if (error.code === 'messaging/invalid-registration-token' ||
//                 error.code === 'messaging/registration-token-not-registered') {
//                 tokensToRemove.push(allTokens.ref.child(tokens[index]).remove());
//             }
//         }
//     });
//         return Promise.all(tokensToRemove);
//     });
//     }
//     });
// });

//Stock# Shape Size Color Clar Cut $ / ct Rap Lab Polish Symm.Fluor.Seller Phone
//OS488 - 18 Round 1.01 I VS1 EX $3, 953 - 41 % GIA EX EX S HVK INTERNATIONAL PVT LTD.--02266449999
//R16 - 2355 Round 1.05 I VS1 EX $3, 953 - 41 % GIA EX EX SB Disons Gems Inc--1 212 921 4133
//U - 601 Round 1.01 I VS1 EX $3, 953 - 41 % GIA EX EX S UNIQUE GEMS--91 22 40178888
//YW1K157A Round 1 I VS1 EX $3, 953 - 41 % GIA EX EX S MIHIR GEMS-- + 9122 23635508


function createPriceStatQuery_(whereClause) {
	var btQueryStr =
		'SELECT ' +
		'Count(*) Count, ' +
		'MIN(Rate_US) min_price, ' +
		'MAX(Rate_US) max_price, ' +
		'AVG(Rate_US) avg_price, ' +
		'Shape, ' +
		'Size, ' +
		'Color, ' +
		'Clarity, ' +
		'Cut,  ' +
		'Polish, ' +
		'Sym, ' +
		'Flour, ' +
		'FIRST(ReportNo) ReportNo'
	'FROM Diamond_Inv.latest ' +
	'WHERE ' +
	whereClause.join(' AND \n') +
		'GROUP BY ' +
		'Size, ' +
		'Shape, ' +
		'Color, ' +
		'Clarity, ' +
		'Cut,  ' +
		'Polish, ' +
		'Sym, ' +
		'Flour ' +
		'ORDER BY avg_price, size, ' +
		'Shape, ' +
		'Color, ' +
		'Clarity, ' +
		'Cut,  ' +
		'Polish, ' +
		'Sym, ' +
		'Flour ' +
		'LIMIT 30;'

	var btQuery = {
		query: btQueryStr
	};
	return btQuery;
}