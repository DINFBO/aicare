<template>
  <div class="alarm">
    <div class="alarm__title">
      <span>내 알람</span>
      <span class="close-btn" @click="$emit('closeAlarmModal')"
        ><i class="fas fa-times"></i
      ></span>
    </div>
    <hr />
    <ul class="alarm__content">
      <li>
        <span>새로운 댓글이 있습니다.</span>
        <span class="alarm__timestamp"> 2021-10-04 </span>
      </li>
    </ul>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.alarm {
  box-sizing: border-box;
  width: 100vw;
  height: 100vh;
  padding: 0 16px;
  position: fixed;
  top: 0;
  left: 0;
  background-color: $white;
  z-index: 999;

  hr {
    color: $gray;
    margin: 0 auto;
  }

  &__title {
    height: 57px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: $heading;

    .close-btn {
      position: absolute;
      right: 16px;
    }
  }
  &__content {
    padding: 16px 0;

    li {
      list-style-type: disc;
      list-style-position: inside;
      color: $yellow;
      position: relative;

      span {
        color: $black;
      }

      span:last-child {
        color: $gray;
        font-size: $description;
        position: absolute;
        right: 0;
        bottom: 0;
      }
    }
  }
}
</style>
