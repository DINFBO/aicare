<template>
  <nav class="nav">
    <div class="nav__icon">
      <NuxtLink to="/"><i class="fas fa-home"></i></NuxtLink>
    </div>
    <div class="nav__icon">
      <NuxtLink to="/analysis"><i class="fas fa-chart-line"></i></NuxtLink>
    </div>
    <div class="nav__icon">
      <NuxtLink to="/history"><i class="far fa-calendar"></i></NuxtLink>
    </div>
    <div class="nav__icon">
      <NuxtLink to="/config"><i class="fas fa-cog"></i></NuxtLink>
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

  box-shadow: rgba(50, 50, 93, 0.25) 0px -2px 5px -1px;

  &__icon {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  a {
    color: $gray;
  }
  a.nuxt-link-exact-active {
    color: $black;
  }
}
</style>
