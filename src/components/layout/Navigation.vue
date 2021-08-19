<template>
  <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link class="navbar-item" to="/">
        <img src="https://www.svgrepo.com/show/120941/tomato.svg" />
        <h3 class="navbar-item title is-3 has-text-light">Tomatos</h3>
      </router-link>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <template v-if="user">
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link"> {{user.email}} </a>
            <div class="navbar-dropdown">
              <router-link class="navbar-item" to="/config"> Config </router-link>
              <a class="navbar-item" @click.prevent="logout"> Log Out </a>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="buttons">
            <router-link class="button is-danger" to="/">
            <strong>Login</strong>
            </router-link>
          </div>
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
import firebase from "firebase";
export default {
  data() {
    return {
      user: null
    };
  },
  methods: {
    logout() {
      firebase.auth().signOut().then(() => {
          this.$router.push({ name: "login" });
        })
    },
  },
  created() {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        this.user = user
      } else {
        this.user = null
      }
    });
  },
}
</script>