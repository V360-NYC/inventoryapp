import { firestoreDB } from '../../config/firebase.js';

export const postQuery = (path, data) => {
    firestoreDB.collection(path).add(data)
    .then(response => {

    })
    .catch(err => console.error(err))
}

export const loadMessages = (path) => {
    firestoreDB.collection(path)
    .onSnapshot(change => {
        
    })
    
}

export const addFileMetaData = (collectionName, docID, data) => {
    return firestoreDB.collection(collectionName).doc(docID)
            .update(data)
}

export const getUserVendors = (uid) => {
    return firestoreDB.collection(`userVendors`).where('userID','==',uid).get()
    .then(response => {
        return response.docs.map(doc => {
            return doc.data();
        })
    })
    .catch(err=>err)
}
