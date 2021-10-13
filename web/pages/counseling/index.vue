<template>
  <div class="container">
    <h1>상담 신청하기</h1>
    <ul>
      <li>
        <div class="counselor">
          <img src="" alt="" />
          <div class="counselor__info">
            <span class="counselor__name">유상우 원장</span>
            <span class="counselor__category"
              >공황장애, 사회불안장애, 인지행동치료</span
            >
          </div>
        </div>
        <div class="apply-btn">신청하기</div>
      </li>
    </ul>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.container {
  padding: 32px 16px 16px;
  height: $page-height;

  h1 {
    font-size: $heading;
    font-weight: bold;
  }

  .counselor {
    // display: flex;
    // justify-content: space-between;
    // align-items: center;

    img {
      width: 50px;
      height: 50px;
      border-radius: 5px;
      margin-right: 16px;
    }

    &__info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }

    &__name {
      font-weight: bold;
      margin-bottom: 8px;
    }
    &__category {
      font-size: $description;
    }
  }
  .apply-btn {
    width: 100%;
    padding: 16px 0;
    text-align: center;
    font-size: $sub-heading;
  }
}
</style>
