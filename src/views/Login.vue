<template>
  <form
    action="#"
    @submit.prevent="login"
    class="box container mt-6 p-4 is-rounded"
  >
    <h2 class="title">Login</h2>
    <hr />
    <div class="field">
      <label class="label">Email</label>
      <div class="control">
        <input
          class="input is-rounded"
          type="email"
          placeholder="e.g. mail@example.com"
          v-model="email"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">Password</label>
      <div class="control">
        <input
          class="input is-rounded"
          type="password"
          placeholder="********"
          v-model="password"
        />
      </div>
    </div>

    <button type="submit" class="button is-danger is-fullwidth is-rounded mt-4">
      Log in
    </button>
  </form>
  <div class="container notification is-danger" v-if="error">
    {{ error }}
  </div>
</template>

<script>
// @ is an alias to /src
import '@/firebase/init'
import firebase from "firebase"
export default {
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  name: "Login",
  methods: {
    login() {
      if (this.email && this.password) {
        firebase
          .auth()
          .signInWithEmailAndPassword(this.email, this.password)
          .then(() => {
            this.$router.push({ name: "config" });
          })
          .catch((err) => {
            this.error = err.message;
          });
      } else {
        this.error = "All fields required";
      }
    },
  },
};
</script>
