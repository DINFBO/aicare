<template>
  <div class="app">
    <NavBar />
    <Nuxt />
  </div>
</template>

<script>
import NavBar from '../components/NavBar.vue'

export default {
  components: { NavBar },
}
</script>

<style scoped>
.app {
  height: 100vh;
  box-sizing: border-box !important;
}
</style>
