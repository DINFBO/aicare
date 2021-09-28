<template>
  <div class="app">
    <Header />
    <Nuxt />
  </div>
</template>

<script>
import Header from '../components/Header.vue'

export default {
  components: { Header },
}
</script>

<style scoped>
.app {
  height: 100vh;
  box-sizing: border-box !important;
}
</style>
