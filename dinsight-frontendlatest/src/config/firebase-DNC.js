import firebase from 'firebase/app';
import 'firebase/auth';

import 'firebase/firestore';
import 'firebase/database';
import 'firebase/storage';
import 'firebase/functions';

const firebaseConfig = {
  apiKey: "AIzaSyD9Xx6J2WHNz9vV_TWOia1TL7xhqi-jnqw",
  authDomain: "friendlychat-bb9ff.firebaseapp.com",
  databaseURL: "https://friendlychat-bb9ff-default-rtdb.firebaseio.com",
  projectId: "friendlychat-bb9ff",
  storageBucket: "friendlychat-bb9ff.appspot.com",
  messagingSenderId: "832382376139",
  appId: "1:832382376139:web:f55b30c7def892db5f634e",
  measurementId: "G-72E3EDMELK"
};
firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();

export const authProviders = {
  googleAuthProvider: new firebase.auth.GoogleAuthProvider()
}

export const realtimeDB = firebase.database();

export const firestoreDB = firebase.firestore();

export const storage = firebase.storage();

export const functions = firebase.functions();

export const query = firestoreDB.query;

export const where = firestoreDB.where;

export const doc = firestoreDB.doc;

export const getDoc = firestoreDB.getDoc;

export const collection = firestoreDB.collection;

export default firebase;
