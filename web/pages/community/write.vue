<template>
  <div class="container">
    <div class="title">작성하기</div>
    <div class="form">
      <input
        v-model="title"
        type="text"
        placeholder="제목을 입력하세요"
        required
      />
      <textarea v-model="content" cols="30" rows="10" required></textarea>
      <div class="form__btn">
        <button @click="handleSubmit">저장</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      content: '',
    }
  },
  methods: {
    handleSubmit() {
      console.log(this.title, this.content)
      this.title = ''
      this.content = ''
      this.$router.push('/community')
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: $page-height;
  padding: 16px;

  .title {
    font-size: $heading;
    font-weight: bold;
    padding-top: 16px;
    margin-bottom: 24px;
  }

  .form {
    display: flex;
    flex-direction: column;

    input,
    textarea,
    button {
      border: none;
      background-color: rgba(245, 223, 77, 0.3);
    }

    input {
      box-sizing: border-box !important;
      color: $gray;
      margin: 8px 0;
      padding: 8px;
      font-size: 16px;
    }

    textarea {
      color: $gray;
      padding: 8px;
      font-size: 16px;
    }

    .form__btn {
      display: flex;
      justify-content: flex-end;
      button {
        color: $white;
        background-color: $yellow-darken;
        padding: 10px 24px;
        border-radius: 5px;
        font-size: $sub-heading;
        font-weight: bold;
      }
    }

    textarea {
      margin: 16px 0;
    }
  }
}
</style>
