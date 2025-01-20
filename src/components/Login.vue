<template>
    <div class="login-page">
      <div class="login-container">
        <h2>Login</h2>
        <form @submit.prevent="register">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <p v-if="errMsg">{{ errMsg }}</p>
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';  // <-- Add this import
  import { getAuth, signInWithEmailAndPassword } from 'firebase/auth';
  import { inject } from 'vue';
  import {useRouter} from 'vue-router';

  
  export default {
    name: "UserLogin",
    setup() {
      const auth = inject('auth');
      const username = ref('');
      const password = ref('');
      const router = useRouter();
      const errMsg = ref()

      const register = () => {
        const auth = getAuth();
        signInWithEmailAndPassword(auth, username.value, password.value)
          .then(() => {
            console.log("Succesfully signed in!");

            console.log(auth.currentUser);
            router.push('#/dashboard').then(() => {
              window.location.reload();
            });

            //router.push("/#/dashboard")
          })
          .catch((error) => {
            console.log(error.code);
            alert(error.message)
          }
        )
      }
  
      const handleLogin = async () => {
        if (!auth) {
          console.error("Firebase auth is not available");
          return;
        }
  
        try {
          // Use Firebase Authentication to log in
          const userCredential = await signInWithEmailAndPassword(auth, username.value, password.value);
          const user = userCredential.user;
          console.log("User logged in:", user);
  
          // Redirect to the dashboard
          this.$router.push('/dashboard');
        } catch (error) {
          switch(error.code){
            case "auth/invalid-email":
              errMsg.value = "Invalid email";
              break;
              case "auth/user-not-found":
              errMsg.value = "No account with that email was found";
              break;
              case "auth/wrong-password":
              errMsg.value = "Incorrect password";
              break;
            default:
              errMsg.value = "Email or password was incorrect";
              break;
          }
          console.error("Login error:", error.message);
          alert("Invalid username or password");
        }
      };
  
      return {
        username,
        password,
        handleLogin,
        register
      };
    },

    methods: {
    // Navigate to dashboard when button is clicked
    navigateToDashboard() {
      this.$router.push('/dashboard');
    }}
  };
  </script>
  
  <style scoped>
  .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f9f9f9;
  }
  .login-container {
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  .form-group {
    margin-bottom: 15px;
  }
  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
  </style>
  