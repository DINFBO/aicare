<template>
  <div>
    <div class="main">
      <div class="main__box">AI CARE</div>
      <div>
        {{isMdOrSm}}
        {{isLargeThanSm}}
        {{isSmallThanMd}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isMdOrSm() {
      return this.$breakpoints.md || this.$breakpoints.sm
    },
    isLargeThanSm() {
      return this.$breakpoints.lSm // Is Large than sm include sm
    },
    isSmallThanMd() {
      return this.$breakpoints.sMd // Is Small than md include md
    },
  },
}
</script>

<style lang="scss" scoped>
.main {
  height: 100vh;
  background-color: $gray;
  &__box {
    color: $primary;
    font-size: 24px;
  }
}
</style>
