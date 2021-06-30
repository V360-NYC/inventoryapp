const functions = require("firebase-functions");
const admin = require('firebase-admin');
const {Storage} = require('@google-cloud/storage');
 
admin.initializeApp({
    credential : admin.credential.applicationDefault()
});

const db = admin.firestore()

exports.updateInventoryFilePointer = functions.storage.bucket('dinsight-user-inventory-test').object().onFinalize((object) => {
    const uid = object.name.split('/')[0];

    const collectionRef = db.collection(`fileMeta/${uid}/inventoryFiles`);

    const storage = new Storage();
    const bucket = storage.bucket('dinsight-user-inventory-test');

    const file = bucket.file(object.name);

    const downloadURL = await file.get  

    collectionRef.add({
        createdAt : admin.firestore.Timestamp.fromDate(new Date(object.name)),
        path : object.name,
        downloadURL = await 
    })
})
