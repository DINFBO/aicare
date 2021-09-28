<template>
  <div class="container">
    <div class="user">
      <span class="user__title">안녕하세요 OOO님!</span>
      <span class="user__subtitle">전역까지 177일 남았습니다.</span>
      <div class="user__img">
        <div></div>
      </div>
    </div>
    <div class="main">
      <!-- <div class="recent-diary">
        <div class="title title--bold">
          <span>최근 일기</span>
        </div>
        <ul>
          <li>
            <span class="recent-diary__title">오늘은 힘든 날이다...</span>
            <span class="recent-diary__play-btn"
              ><i class="far fa-play-circle"></i
            ></span>
          </li>
        </ul>
      </div> -->
      <div class="hits-posts">
        <div class="title title--bold">
          <span>인기글</span>
        </div>
        <ul>
          <li>
            <span class="hits-posts__title">오늘은 힘든 날이다...</span>
            <span class="hits-posts__timestamp">09/26 22:58</span>
          </li>
          <li>
            <span class="hits-posts__title">오늘은 힘든 날이다...</span>
            <span class="hits-posts__timestamp">09/26 22:58</span>
          </li>
          <li>
            <span class="hits-posts__title">오늘은 힘든 날이다...</span>
            <span class="hits-posts__timestamp">09/26 22:58</span>
          </li>
        </ul>
      </div>
      <!-- <div class="goto">
        <div class="goto__write-diary">
          <span class="goto__title">오늘은 어떤 일이 있으셨나요?</span>
          <button class="goto__btn">일기 쓰러 가기</button>
        </div>
        <div class="goto__show-analysis">
          <span class="goto__title"
            >일기를 쓰셨다면 나의 감정변화를 확인해보세요.</span
          >
          <button class="goto__btn">분석결과 보러가기</button>
        </div>
        <div class="goto__comunity">
          <span class="goto__title">다른 사람들과 고민을 나눠보세요</span>
          <button class="goto__btn">커뮤니티로 가기</button>
        </div>
      </div> -->
      <div class="goto">
        <span class="goto__title">오늘은 어떤 일이 있으셨나요?</span>
        <span class="goto__btn">일기 쓰러 가기</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

.container {
  // font-family: 'Nanum Pen Script', cursive;
  font-family: 'Gowun Dodum', sans-serif;
  box-sizing: border-box !important;
  padding: 32px 16px;
  height: calc(100vh - 57px);
  .title {
    font-size: 16px;
    margin-bottom: 20px !important;

    &--bold {
      font-weight: bold;
      color: #e6c823;
    }
  }

  .user {
    // height: 48px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    &__title {
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 10px !important;
    }
    &__subtitle {
      font-size: 14px;
    }
    &__img {
      display: flex;
      justify-content: center;
      margin-top: 32px !important;

      div {
        width: 170px;
        height: 170px;
        border-radius: 50%;
        background-color: #e6c823;
      }
    }
  }

  .main {
    height: 30vh;
    min-height: 250px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    margin-top: 70px !important;
  }

  .recent-diary {
    width: 100%;
    box-sizing: border-box !important;
    padding: 12px 16px;
    // border: 1px solid rgb(147, 149, 151);
    // border: 1px solid rgba(147, 149, 151, 0.3);
    box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
    border-radius: 5px;

    ul {
      li {
        display: flex;
        justify-content: space-between;
        margin: 10px 0 !important;
      }
    }
  }

  .hits-posts {
    width: 100%;
    box-sizing: border-box !important;
    padding: 12px 16px;
    // border: 1px solid rgb(147, 149, 151);
    // border: 1px solid rgba(147, 149, 151, 0.3);
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
    border-radius: 5px;

    ul {
      li {
        display: flex;
        justify-content: space-between;
        margin: 12px 0 !important;
      }
    }

    &__timestamp {
      font-size: 12px;
      color: #939597;
    }
  }

  .goto {
    width: 100%;
    padding: 24px 0;
    background-color: #f9f0af;
    box-sizing: border-box !important;
    // height: 160px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;

    &__write-diary,
    &__show-analysis,
    &__comunity {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      margin: 12px 0 !important;

      span {
        max-width: 60%;
        word-break: keep-all;
      }

      button {
        font-family: 'Gowun Dodum', sans-serif;
        width: 120px;
        height: 40px;
        word-break: keep-all;
        background-color: #e6c823;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        font-size: 14px;
      }
    }
  }
}
</style>
