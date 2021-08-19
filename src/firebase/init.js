import firebase from 'firebase'

// Your web app's Firebase configuration
const fbConfig = {
    apiKey: "AIzaSyBqORZ0byKbT8xEB5ezkcwytcc9Q2fgwiY",
    authDomain: "tomatos-w.firebaseapp.com",
    databaseURL: "https://tomatos-w-default-rtdb.firebaseio.com",
    projectId: "tomatos-w",
    storageBucket: "tomatos-w.appspot.com",
    messagingSenderId: "723804813778",
    appId: "1:723804813778:web:20913bc73667be898db00b"
};

const app = firebase.initializeApp(fbConfig);

export default app

