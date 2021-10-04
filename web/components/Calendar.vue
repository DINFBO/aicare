<template>
  <div>
    <no-ssr>
      <v-calendar
        :attributes="attrs"
        mode="date"
        is-expanded
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
      this.$router.push(`history/${day.id}`)
    },
  },
}
</script>

<style lang="scss" scoped>
div {
  &::v-deep .vc-container {
    border: none;
    border-radius: 5px;

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
