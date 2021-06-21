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