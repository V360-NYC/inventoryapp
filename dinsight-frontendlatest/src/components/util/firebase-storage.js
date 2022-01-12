
import { storage } from "../../config/firebase";

export const uploadToStorage = (filepath, file) => {
    return storage.refFromURL(`gs://${filepath}`).put(file)
    
}

export const listBucketObjects = (path) => {
    return storage.refFromURL(`gs://${path}`).listAll()
}