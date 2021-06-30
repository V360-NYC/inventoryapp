/*
 * This file contains all the code that was removed or being used for testing but no longer userful.
 */

function writeInvDataToFirestore (uid, queryMode, ts, companyCodeCounterParam) {
	var companyIndex = companyCodeCounterParam;
	if (companyIndex >= gConst.companyCode.length ) {
		return;
	}
//	for (var sizeIndex = 0; sizeIndex + 1 < gConst.sizeRange.length; ) {
//	var sizeIndex = 2;
		var companyCode = gConst.companyCode[companyIndex];
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
				'ROUND(Rate_US) Rate_US, ' +
				'ROUND((Rate_US)/Size)  USDPerCT, ' +
				'Back, ' +
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
			'WHERE Rate_US != 0 AND ' +
				'CompanyCode ="' + companyCode + '"'
//				+ ' AND Size >= ' + gConst.sizeRange[sizeIndex] + ' AND ' +
//				' Size < ' + gConst.sizeRange[sizeIndex + 1]
				;
				
//		sizeIndex++;
		console.log("Query is:" + btQueryStr);

	
		// Given that query is generated correctly.
		const bqOptions = {
			query: btQueryStr,
			useLegacySql: true // Use standard SQL syntax for queries.
		};
		replyUser_(uid, queryMode, ts, 'Firestore ETL status:', 'Starting for ' + companyCode, '');
	
		// Runs the query as a job
		// Link to sample code: https://cloud.google.com/bigquery/create-simple-app-api#bigquery-simple-app-query-nodejs
		bigquery
			.query(bqOptions)
			.then((results) => {
				const rows = results[0];
				replyUser_(uid, queryMode, ts, 'Firestore ETL status:', 'Successfully finish for ' + companyCode  + " length: "+ rows.length , '');
				firestoreUtil.AddToFirestore(firestoreDb, rows, companyCode);
				replyUser_(uid, queryMode, ts, 'Firestore ETL status:', 'Successfully finished writing to FireStore for ' + companyCode  + " length: "+ rows.length, '');				
//				if (sizeIndex + 1 === gConst.sizeRange.length) { // To make sure that writeInvData is only called once for new company
					writeInvDataToFirestore(uid, queryMode, ts, companyIndex++); // Start populating for next company.
//				}
		   }).catch((err) => {
				console.error('User Search BQ ERROR:', err);
				replyUser_(uid, queryMode, ts, 'Firestore ETL status:', 'Failed for ' + companyCode + ' and error was: ' + err, '');
//				if (sizeIndex + 1 === gConst.sizeRange.length) { // To make sure that writeInvData is only called once for new company
//					writeInvDataToFirestore(uid, queryMode, ts, companyIndex++); // Start populating for next company.
//				}
			});
//	}

}

