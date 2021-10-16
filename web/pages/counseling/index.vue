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
        <div class="apply-btn">
          <nuxt-link to="/counseling/유상우원장">신청하기</nuxt-link>
        </div>
      </li>
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
        <div class="apply-btn">
          <nuxt-link to="/counseling/유상우원장">신청하기</nuxt-link>
        </div>
      </li>
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
        <div class="apply-btn">
          <nuxt-link to="/counseling/유상우원장">신청하기</nuxt-link>
        </div>
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
    margin-bottom: 36px;
  }

  ul {
    li {
      margin: 24px 0;
      .counselor {
        display: flex;
        align-items: center;

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
        box-sizing: border-box;
        width: 100%;
        margin: 8px 0;
        padding: 8px 0;
        text-align: center;
        font-size: $sub-heading;
        background-color: #c7c7c7;
        border-radius: 5px;
      }
      a {
        box-sizing: border-box;
        text-decoration: none;
        color: $black;
      }
    }
  }
}
</style>
