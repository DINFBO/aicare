<template>
  <div class="comment">
    <div class="comment__profile">
      <div class="author">
        <img src="" alt="" />
        <span>박OO</span>
      </div>
      <span class="timestamp"> 2021-10-05 </span>
    </div>
    <div class="comment__content">
      <span>제발 손절해... 정신에 해로울뿐인 동기는 절대네버</span>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.comment {
  margin: 16px 0;

  &__profile {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 6px;

    .timestamp {
      font-size: $description;
      color: $gray;
    }
  }
}
</style>
