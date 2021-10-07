<template>
  <div class="post">
    <div>
      <div class="post__title">
        <span>제목제목제목제목</span>
      </div>
      <div class="post__create">
        <div class="post__author">
          <span class="author-img"><i class="far fa-user"></i></span>
          <span>김OO</span>
        </div>
        <div class="post__timestamp">2021-10-05</div>
      </div>
    </div>
    <button class="post__recommend">
      <span><i class="fas fa-thumbs-up"></i></span>
      5
    </button>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.post {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  min-height: 50px;
  margin: 24px 0;
  cursor: pointer;

  div:first-child {
    flex: 1;
  }
  &__title {
    font-size: $sub-heading;
    font-weight: bold;
    margin-bottom: 8px;
  }
  &__create {
    display: flex;
    justify-content: space-between;
    font-size: 16px;
  }
  &__author {
    display: flex;
    align-items: center;
    .author-img {
      font-size: 14px;
      margin-right: 6px;
    }
  }

  &__recommend {
    box-sizing: border-box;
    width: 50px;
    padding: 4px 6px;
    margin-left: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: $description;
    font-weight: bold;
    color: $recommend;
    border: 1px solid $recommend;
    border-radius: 3px;

    span:first-child {
      margin-right: 5px;
    }
  }
}
</style>
