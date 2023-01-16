import firebase from 'firebase/app';
import 'firebase/auth';

import 'firebase/firestore';
import 'firebase/database';
import 'firebase/storage';
import 'firebase/functions';

const firebaseConfig = {
  apiKey: "AIzaSyAGomuku47SuSiujhi2lMSEcjHVPLUbB_o",
  authDomain: "kp-assist.firebaseapp.com",
  databaseURL: "https://kp-assist-default-rtdb.firebaseio.com",
  projectId: "kp-assist",
  storageBucket: "kp-assist.appspot.com",
  messagingSenderId: "354699324913",
  appId: "1:354699324913:web:9c804c009cf103c65a6850",
  measurementId: "G-95R86VT0XS"
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
