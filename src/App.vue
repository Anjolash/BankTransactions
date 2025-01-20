<template>
  <component :is="currentView" />
</template>

<script setup>
//import Login from './components/Login.vue';
import { ref, computed, onMounted } from 'vue'


//import HelloWorld from './components/HelloWorld.vue'
//import Dashboard from './components/Dashboard.vue';
import Login from './components/Login.vue';
import NotFound from './components/NotFound.vue';
import Dashboard from './components/Dashboard.vue';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
//import { reject, resolve } from 'core-js/fn/promise';

const routes = {
  '/': Login,
  '/dashboard': Dashboard,
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => { 
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  const route = routes[currentPath.value.slice(1) || '/'];
  if(!isLoggedIn.value && route == Dashboard){
    return Login;
  }
  return  route || NotFound;
})
/*
const getCurrentUser = () => {
  return new Promise((resolve, reject) => {
    const removeListener = onAuthStateChanged(
      getAuth(),
      (user) => {
        removeListener();
        resolve(user);
      },
      reject
    )
  })
}*/

const isLoggedIn = ref(false);

let auth;
onMounted(() => {
  auth = getAuth();
  onAuthStateChanged(auth, (user) => {
    if(user){
      console.log("userrr", user)
      isLoggedIn.value = true;
    } else{
      isLoggedIn.value = false;
    }
  })
})

</script>

<style>


@import url('https://fonts.googleapis.com/css2?family=Amarante&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

html, body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

#app {
  font-family: 'Plus Jakarta Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  margin: 0px;
  padding: 0px;
}
</style>

