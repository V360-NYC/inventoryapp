import { realtimeDB } from '../../config/firebase';

export const postQuery = (path, data) => {
    return realtimeDB.ref(path).push(data)
}

export const loadMessages = (path, callback) => {
    realtimeDB.ref(path).limitToLast(12).on('child_added', snapshot => {
        callback({key: snapshot.key, ...snapshot.val()})
    })
    
}
