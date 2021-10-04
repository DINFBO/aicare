<template>
  <div>
    <header class="header">
      <div class="header__title">
        <NuxtLink to="/">AI CARE</NuxtLink>
      </div>
      <div class="header__alarm">
        <span @click="showAlarmModal"><i class="far fa-bell"></i></span>
        <div class="alarm-circle"></div>
      </div>
    </header>
    <alarm-modal v-if="isModalOpened" @closeAlarmModal="isModalOpened=false" />
  </div>
</template>

<script>
import AlarmModal from './AlarmModal.vue'

export default {
  components: { AlarmModal },
  data() {
    return {
      isModalOpened: false,
    }
  },
  methods: {
    showAlarmModal() {
      this.isModalOpened = true
    },
  },
}
</script>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap');
.header {
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 0px 0px 5px 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
  color: $gray;

  &__title {
    font-weight: 700;
    font-size: $heading;
    font-family: 'Caveat', cursive;
  }

  &__alarm {
    font-size: $heading;
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
