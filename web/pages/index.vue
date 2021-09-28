<template>
  <div class="container">
    <div class="user">
      <span class="user__title">안녕하세요 OOO님!</span>
      <span class="user__subtitle">전역까지 177일 남았습니다.</span>
    </div>
    <div class="main">
      <div class="recent-diary">
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
      </div>
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
      <div class="goto">
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
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  box-sizing: border-box !important;
  padding: 32px 16px;
  height: calc(100vh - 57px);
  .title {
    font-size: 16px;
    margin-bottom: 20px !important;

    &--bold {
      font-weight: bold;
    }
  }

  .user {
    height: 48px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;

    &__title {
      font-size: 24px;
      font-weight: bold;
    }
    &__subtitle {
      font-size: 14px;
    }
  }

  .main {
    height: 60vh;
    max-height: 500px;
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
    border: 2px solid rgb(147, 149, 151);
    border: 2px solid rgba(147, 149, 151, 0.3);
    border-radius: 5px;

    ul {
      li {
        display: flex;
        justify-content: space-between;
        margin: 8px 0 !important;
      }
    }
  }

  .hits-posts {
    width: 100%;
    box-sizing: border-box !important;
    padding: 12px 16px;
    border: 2px solid rgb(147, 149, 151);
    border: 2px solid rgba(147, 149, 151, 0.3);
    border-radius: 5px;

    ul {
      li {
        display: flex;
        justify-content: space-between;
        margin: 8px 0 !important;
      }
    }

    &__timestamp {
      font-size: 12px;
      color: #939597;
    }
  }

  .goto {
    width: 100%;
    box-sizing: border-box !important;
    height: 160px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;

    &__write-diary,
    &__show-analysis,
    &__comunity {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      margin: 8px 0;

      span {
        max-width: 60%;
        word-break: keep-all;
      }

      button {
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
