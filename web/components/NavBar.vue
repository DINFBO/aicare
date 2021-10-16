<template>
  <nav class="nav">
    <div class="nav__icon">
      <NuxtLink to="/" exact><i class="fas fa-home"></i></NuxtLink>
    </div>
    <div class="nav__icon">
      <NuxtLink to="/history"><i class="far fa-calendar"></i></NuxtLink>
    </div>
    <div class="nav__icon">
      <NuxtLink to="/community"><i class="fab fa-slideshare"></i></i></NuxtLink>
    </div>
    <div class="nav__icon">
      <NuxtLink to="/counseling"><i class="fas fa-hospital-user"></i></NuxtLink>
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
  a.nuxt-link-active {
    color: $black;
  }
}
</style>
