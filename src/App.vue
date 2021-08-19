<template>
  <div class="app">
    <div id="nav">
      <Navigation />
    </div>
  </div>
  <router-view />
</template>

<script>
import Navigation from './components/layout/Navigation.vue'
export default {
  components: {
    Navigation
  }
}
</script>
<style lang="scss">
  @import './scss/app.scss';
</style>