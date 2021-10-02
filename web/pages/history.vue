<template>
  <div class="container">
    <div class="feelings">
      <span class="feelings__sad">우울: 3</span>
      <span class="feelings__happy">기쁨: 3</span>
      <span class="feelings__annoyance">짜증: 5</span>
      <span class="feelings__angry">화남: 2</span>
    </div>
    <div class="calendar">
      <no-ssr>
        <v-calendar
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
      // eslint-disable-next-line no-console
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

  .calendar {
    height: 60vh;

    .vc-container {
      border: none;
    }
  }
}
</style>
