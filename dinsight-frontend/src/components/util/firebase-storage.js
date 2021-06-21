
import { storageRef } from "../../config/firebase";

export const uploadToStorage = (filepath, file) => {
    return storageRef.child(filepath).put(file)
    
}