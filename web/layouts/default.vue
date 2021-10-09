<template>
  <div class="app">
    <Header />
    <transition name="fade">
      <Nuxt />
    </transition>
    <NavBar />
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import NavBar from '../components/NavBar.vue'

export default {
  components: { Header, NavBar },
}
</script>

<style scoped>
.app {
  height: 100vh;
  box-sizing: border-box !important;
}
</style>
