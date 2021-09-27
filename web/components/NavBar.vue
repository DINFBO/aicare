<template>
  <nav class="nav">
    <div class="nav__title">
      <span>AI CARE</span>
    </div>
    <div class="nav__alarm">
      <span><i class="far fa-bell"></i></span>
    </div>
  </nav>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.nav {
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 0px 0px 5px 5px;
  // box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  box-shadow: 0px 3px 15px 2px rgba(155, 155, 155, 0.6);

  &__title {
    color: $yellow;
    font-weight: bold;
    font-size: 24px;
  }

  &__alarm {
    font-size: 24px;
    color: $gray;
  }
}
</style>
