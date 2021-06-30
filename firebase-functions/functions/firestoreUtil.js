/*
 * AddToFirestore take firebase instance objext, result from bigquery and collection name.
 * It write to firestore the data presennt in bigquery result into collection name with 
 * document being regular counter.
 */
exports.AddToFirestore = function(firestoreDb, bqRows, collectionStr) {
	if (bqRows.length === 0) {
		return;
	}
	var batch = firestoreDb.batch();
	var counter = 0;	
	for (var i = 0; i < bqRows.length; i++) {
		var bqRow = bqRows[i];
		if ('ReportNo' in  bqRow) {
			var docRef = firestoreDb.collection(collectionStr).doc(bqRow['ReportNo']);
			counter++;
			batch.set(docRef, bqRow);
		}
		if (counter % 500 === 0) { // Batch can handler maximum of 500 operations.
			batch.commit();
			batch = firestoreDb.batch();
			console.log('Loaded: ' + collectionStr + ' Number of rows:' + counter);
		}
	}
	batch.commit();
	console.log('Completed loading data for ' + collectionStr + ' Number of rows:' + counter);
};

/*
 * Test reading firestore. 
 */
exports.FirestoreRead = function(uid, queryMode, ts, firestoreDb, replyUserCB_) {
	console.log("FireStore Read Test");
	var invRef = firestoreDb.collection('Dharam_Inv');
	var query = invRef.where('Shape', '==', 'ROUND').limit(10)
		.get()
		.then((snapshot) => {
			var data = [];
			snapshot.forEach(doc => {
				data.push(doc.data());
			});
			console.log('Doc count: '+ data.length);
			replyUserCB_(uid, queryMode, ts, 'FireStoreTestQuery:count', 'Doc Json: ' + JSON.stringify(data), ' ');
		})
		.catch((err) => {
			console.log('Error getting documents', err);
			replyUserCB_(uid, queryMode, ts, 'FireStoreTestQuery:json', 'FireStore Error getting documents', '');
		});

	console.log("FireStore Test 4");
};

/*
 * Another test function.
 */
// TODO: Need to come up with better way of refreshing cache. 
// It should be updated whenever new inventory is uploaded.
function quickSearchRespondFireStore(firestoreDb, uid, queryMode, ts) {
	var cacheDocRef = firestoreDb.collection('cache').doc('quick_search');
	var getDoc = cacheDocRef.get().then(doc => {
        if (!doc.exists) {
            console.log('FireStore --- No such document!');
        	// Given that query is generated correctly.
			const bqOptions = {
				query: QuickSearchQuery,
				useQueryCache: true,
				useLegacySql: true // Use standard SQL syntax for queries.
			};
			bigquery.query(bqOptions).then((results) => {
				const rows = results[0];
				console.log('PT: FireStore 1');
				quickSearchReply(uid, queryMode, ts, rows, null);
				console.log('PT: FireStore 2');
			}).catch((err) => {
				console.error('Quick Search BQ ERROR:', err);
			});
			console.log('FireStore --- Started the query!');
        } else {
            quickSearchReply(uid, queryMode, ts, null, JSON.parse(doc.data()));
        }
    }).catch(err => {
        console.error('Firestore: Error getting document', err);
    });	
}
