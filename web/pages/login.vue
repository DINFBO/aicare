<template>
  <div class="container">
    <div class="login">
      <div class="login__title">
        <span>로그인</span>
      </div>
      <div class="login__form">
        <input type="text" />
        <input type="password" />
        <div class="button">
          <button>로그인</button>
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
}
</script>

<style lang="scss" scoped>
.container {
  box-sizing: border-box !important;
  height: 100vh;
  padding: 50% 16px 47px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;

  .login {
    width: 100%;

    .login__title {
      width: 100%;
      font-size: 28px;
      font-weight: bold;
      color: $gray;
      margin-bottom: 40px !important;
    }

    .login__form {
      width: 100%;
      display: flex;
      flex-direction: column;

      input {
        box-sizing: border-box !important;
        background-color: rgba(245, 223, 77, 0.3);
        color: $gray;
        border: none;
        margin: 8px 0;
        padding: 16px 8px;
        font-size: 16px;
      }

      .button {
        display: flex;
        justify-content: flex-end;

        button {
          font-family: 'Gowun Dodum', sans-serif;
          box-sizing: border-box !important;
          margin-top: 36px;
          padding: 10px 25px;
          font-size: $sub-heading;
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
    // position: absolute;
    // bottom: 0px;
    // z-index: 1;

    em {
      color: #c0aa14;
    }
  }
}
</style>
