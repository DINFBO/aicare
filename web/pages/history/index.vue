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
          :theme="calendarTheme"
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
          highlight: {
            style: {
              background: '#E6C823',
            },
            contentStyle: {
              color: '#ffffff',
            },
          },
          dates: new Date(),
        },
        {
          key: 'writeDay',
          dot: true,
          dates: [],
        },
      ],
      calendarTheme: {
        wrapper: {
          color: '#fd4d3e',
        },
      },
    }
  },
  methods: {
    goDetail(day) {
      this.$router.push(`history/${day.id}`)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: calc(100vh - 57px - 47px);
  padding: 16px;

  .feelings {
    box-sizing: border-box;
    padding: 16px;
    font-weight: bold;
  }

  .calendar {
    &::v-deep .vc-container {
      border: none;
      border-radius: 5px;

      .vc-header {
        padding: 20px 18px;
      }
      .vc-weekday {
        color: $black;
      }
      .vc-day {
        padding: 20px 0;
        color: $gray-darken;
      }
    }
  }
}
</style>
