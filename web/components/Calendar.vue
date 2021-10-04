<template>
  <div>
    <no-ssr>
      <v-calendar
        :attributes="attrs"
        mode="date"
        is-expanded
        :max-date='new Date()'
        @dayclick="goDetail"
      />
    </no-ssr>
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
    }
  },
  methods: {
    goDetail(day) {
      const today = new Date()
      if (day.day <= today.getDate())
        this.$router.push(`history/${day.id}`)
    },
  },
}
</script>

<style lang="scss" scoped>
div {
  padding-top: 16px;
  &::v-deep .vc-container {
    border: none;
    border-radius: 5px;
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;

    .vc-header,
    .vc-arrows-container {
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
</style>
