<template>
  <nav>
    <div class="nav__home">
      <span><i class="fas fa-home"></i></span>
    </div>
    <div class="nav__analysis">
      <span><i class="fas fa-chart-line"></i></span>
    </div>
    <div class="nav__calender">
      <span><i class="far fa-calendar"></i></span>
    </div>
    <div class="nav__config">
      <i class="far fa-calendar"></i>
    </div>
  </nav>
</template>

<style lang="scss" scoped>
nav {
  height: 47px;
  padding: 0 16px;
  font-size: 24px;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;

  div {
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
