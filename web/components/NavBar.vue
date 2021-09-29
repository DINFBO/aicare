<template>
  <nav class="nav">
    <div class="nav__icon nav__icon--active">
      <span><i class="fas fa-home"></i></span>
    </div>
    <div class="nav__icon">
      <span><i class="fas fa-chart-line"></i></span>
    </div>
    <div class="nav__icon">
      <span><i class="far fa-calendar"></i></span>
    </div>
    <div class="nav__icon">
      <i class="fas fa-cog"></i>
    </div>
  </nav>
</template>

<style lang="scss" scoped>
.nav {
  height: 47px;
  padding: 0 16px;
  font-size: 24px;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
  color: $gray;
  border-top: 1px solid $gray;

  &__icon {
    display: flex;
    justify-content: center;
    align-items: center;

    &--active {
      color: black;
    }
  }
}
</style>
