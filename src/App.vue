<template>
  <Dashboard />
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Dashboard from './components/Dashboard.vue';

export default {
  name: 'App',
  components: {
    Dashboard
  }
}
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

