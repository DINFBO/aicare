<template>
  <div class="container">
    <div class="counselor">
      <img src="" alt="" />
      <div class="counselor__info">
        <span class="counselor__name">유상우 원장</span>
        <span class="counselor__category"
          >공황장애, 사회불안장애, 인지행동치료</span
        >
      </div>
    </div>
    <div class="profile">
      <span>정신건강의학과 전문의/의학박사</span>
      <span>연세 정신건강의학과 원장</span>
      <span>연세의대 정신학과 교실 임상/외래교구</span>
      <span>한림의대 정신과학 교실 외래교수</span>
    </div>
    <form>
      <input type="text" required placeholder="제목을 입력하세요" />
      <textarea rows="10" required></textarea>
      <button>제출하기</button>
    </form>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.container {
  padding: 32px 16px 16px;
  height: $page-height;

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

  .profile {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 16px 0 24px;

    span {
      margin: 4px;
    }
  }

  form {
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;

    input {
      width: 100%;
      background-color: $yellow-light;
      font-size: 16px;
      padding: 8px;
    }
    textarea {
      resize: none;
      width: 100%;
      background-color: $yellow-light;
      font-size: 16px;
      padding: 8px;
      border: none;
      margin: 16px 0;
    }
    button {
      background-color: $yellow;
      padding: 10px 25px;
      font-size: $sub-heading;
      font-weight: bold;
      border-radius: 5px;
      color: $gray-darken;
    }
  }
}
</style>
