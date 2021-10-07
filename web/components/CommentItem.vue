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
      <span>제발 손절해... 정신에 해로울뿐인 동기는 네버</span>
      <template v-if="isCommentWritter">
        <button @click="deleteComment"><i class="far fa-trash-alt"></i></button>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isCommentWritter: true,
    }
  },
  methods: {
    deleteComment() {},
  },
}
</script>

<style lang="scss" scoped>
.comment {
  margin: 12px 0;
  padding: 8px;

  &__profile {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 12px;
    font-size: $sub-heading;

    .author {
      img {
        width: 16px;
        height: 16px;
        border-radius: 50%;
      }
    }

    .timestamp {
      font-size: $description;
      color: $gray;
    }
  }

  &__content {
    word-break: keep-all;
    line-height: 1.1;
    display: flex;
    justify-content: space-between;
    align-items: center;

    span {
      max-width: 85%;
    }
    button {
      border: none;
      font-size: 16px;
      color: #a83838;
    }
  }
}
</style>
