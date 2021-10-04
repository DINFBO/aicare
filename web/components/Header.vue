<template>
  <header class="header">
    <div class="header__title">
      <NuxtLink to="/">AI CARE</NuxtLink>
    </div>
    <div class="header__alarm">
      <span><i class="far fa-bell"></i></span>
      <div class="alarm-circle"></div>
    </div>
  </header>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap');
.header {
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 0px 0px 5px 5px;
  // box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  // box-shadow: 0px 3px 15px 2px rgba(155, 155, 155, 0.6);
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
  // background-color: $gray;
  color: $gray;

  &__title {
    font-weight: 700;
    font-size: 24px;
    font-family: 'Caveat', cursive;
  }

  &__alarm {
    font-size: 24px;
    position: relative;

    .alarm-circle {
      position: absolute;
      top: 2px;
      left: 1px;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background-color: $yellow;

    }
  }

  a {
    text-decoration: none;
    color: $gray;
  }
}
</style>
