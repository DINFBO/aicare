<template>
  <div class="container">
    <div class="sign-up">
      <div class="sign-up__title">
        <span>회원가입</span>
      </div>
      <div class="sign-up__form">
        <input type="text" placeholder="아이디" />
        <input type="password" placeholder="비밀번호" />
        <input type="password" placeholder="비밀번호 확인" />
        <label for="input-profile">
          프로필 사진 업로드
          <span>
            <i v-if="isSuccess" class="far fa-check-circle success"></i>
            <i v-else-if="isSuccess == false" class="far fa-times-circle fail"></i>
          </span>
        </label>
        <input id="input-profile" type="file" @change="previewFiles" />
        <div class="button">
          <button>회원가입</button>
        </div>
      </div>
    </div>
    <div class="footer">
      <span>아직 회원이 아니신가요? <em>회원가입</em></span>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'auth',
  data() {
    return {
      isSuccess: null,
    }
  },
  methods: {
    previewFiles(event) {
      if (event.target.files[0] !== null) {
        this.isSuccess = true
      }
    },
  },
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

.container {
  box-sizing: border-box !important;
  font-family: 'Gowun Dodum', sans-serif;
  height: 100vh;
  padding: 50% 16px 47px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;

  .sign-up {
    width: 100%;

    .sign-up__title {
      width: 100%;
      font-size: 28px;
      font-weight: bold;
      color: $gray;
      margin-bottom: 40px !important;
    }

    .sign-up__form {
      width: 100%;
      display: flex;
      flex-direction: column;

      input,
      label {
        background-color: rgba(245, 223, 77, 0.3);
        color: $gray;
        border: none;
        margin: 8px 0;
        padding: 8px;
      }

      label {
        font-weight: bold;
        text-align: center;
        padding: 12px !important;
      }

      #input-profile {
        display: none;
      }

      .button {
        display: flex;
        justify-content: flex-end;

        button {
          font-family: 'Gowun Dodum', sans-serif;
          box-sizing: border-box !important;
          margin-top: 36px;
          padding: 10px 25px;
          font-size: 18px;
          font-weight: bold;
          border: none;
          border-radius: 5px;
          color: #ffffff;
          background-color: $yellow;
        }
      }
    }
  }

  .footer {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    em {
      color: #c0aa14;
    }
  }

  .success {
    color: rgb(45, 172, 45);
  }
  .fail {
    color: red;
  }
}
</style>
