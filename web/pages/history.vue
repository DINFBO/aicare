<template>
  <div class="container">
    <no-ssr>
      <v-date-picker
        v-model="selectedDate"
        mode="range"
        :min-date="new Date()"
        show-caps
      />
    </no-ssr>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedDate: {
        start: new Date(2018, 10, 9),
        end: new Date(2018, 10, 10),
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.container {
  height: 100%;
}
</style>
