import { createApp } from 'vue';
import App from './App.vue';
import router from '../src/router';
import { initializeApp } from 'firebase/app';
//import { getAuth } from 'firebase/auth'
const firebaseConfig = {
  apiKey: 'AIzaSyATJfHqqHNVcYJrm5VrEcD2Q_owgSI1V-Q',
  authDomain: 'bank-e2e35.firebaseapp.com',
  projectId: 'bank-e2e35',
  storageBucket: 'bank-e2e35.firebaseapp.com',
  messagingSenderId: '1008952309284',
  appId: '1:1008952309284:web:13d6e5e52d86d54b3b4ab1',
  measurementId: 'G-6VEM9P5DPV',
};

initializeApp(firebaseConfig);
//const auth = getAuth(firebaseApp);


console.log('Initial route:', router.currentRoute); 
console.log('Route path:', router.currentRoute.value.path);  // This will log the current route path
console.log(router.currentRoute.value)
const app = createApp(App);
app.use(router)
//app.provide('auth', auth);
app.mount('#app');
