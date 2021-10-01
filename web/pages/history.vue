<template>
  <div class="container">
    <div class="calendar">
      <no-ssr>
        <v-date-picker
          :attributes="attrs"
          mode="date"
          is-expanded
          @dayclick="goDetail"
        />
      </no-ssr>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      attrs: [
        {
          key: 'today',
          highlight: 'yellow',
          dates: new Date(),
        },
        {
          key: 'writeDay',
          dot: true,
          dates: [],
        },
      ],
    }
  },
  methods: {
    goDetail(day) {
      // day -> id: 년,월,일, day:일,
      console.log(day)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: calc(100vh - 57px - 47px);
  padding: 16px;
}
</style>
