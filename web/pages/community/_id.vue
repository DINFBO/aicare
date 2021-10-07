<template>
  <div class="container">
    <div class="author">
      <div class="author__profile">
        <span class="img"><i class="fab fa-slideshare"></i></span>
        <div>
          <span>김OO</span>
          <span class="timestamp">2021-10-05</span>
        </div>
      </div>
      <div class="recommend">
        <button @click="recommendPost">
          <span><i class="fas fa-thumbs-up"></i></span>
          {{ recommendCount }}
        </button>
      </div>
    </div>
    <div class="content">
      <div class="content__title">
        <span>제목입니다.</span>
      </div>
      <div class="content__content">
        <p>
          동아리에서 알게된 동기가 자꾸 과제 보내달라그러면 어때? 진짜 짜증나게
          나도 내 시간들여서 하는건데 인스타보면 맨날 술먹고다니느라고 과제할
          시간이 없나봐;;;; 마감당일에 연락오면 그냥 무시하고 다음날에 못봤다고
          핑계댈텐데 항상 마감 3-4일전에 연락와서 안읽씹도 못하게 해 과에
          아는애가 얘밖에 없어서 쌍욕박고 손절할수도없고 짜증난다.
        </p>
      </div>
    </div>
    <div class="comments">
      <div class="comments__write">
        <input type="text" required />
        <div class="comments__submit">
          <button @click="handelCommentSubmit">작성</button>
        </div>
      </div>
      <div class="comments__items">
        <template v-if="isCommentExist">
          <CommentItem v-for="i in 4" :key="i" />
        </template>
        <template v-else>
          <div class="no-comments">댓글을 작성해주세요.</div>
        </template>
      </div>
    </div>
  </div>
</template>
<script>
import CommentItem from '../../components/CommentItem.vue'

export default {
  components: { CommentItem },
  data() {
    return {
      isCommentExist: false,
      recommendCount: 5,
      isRecommend: false,
    }
  },
  methods: {
    recommendPost() {
      if (!this.isRecommend) {
        this.isRecommend = true
        this.recommendCount++
      } else {
        this.isRecommend = false
        this.recommendCount--
      }
    },
    handelCommentSubmit() {
      this.isCommentExist = true
    },
  },
}
</script>
<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: $page-height;
  padding: 16px;
  overflow-y: scroll;

  .author {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;

    .img {
      font-size: 40px;
    }
    &__profile {
      display: flex;
      justify-content: space-between;

      div {
        height: 40px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: flex-start;
        margin-left: 12px;
      }

      .timestamp {
        font-size: $description;
        color: $gray;
      }
    }
    .recommend {
      button {
        font-size: $sub-heading;
        border: 1px solid green;
        border-radius: 5px;
        padding: 8px 16px;
        color: green;
      }
    }
  }

  .content {
    margin-bottom: 16px;

    &__title {
      font-size: $heading;
      margin-bottom: 12px;
    }
    &__content {
      line-height: 1.2;
    }
  }

  .comments {
    padding-top: 16px;
    border-top: 1px solid #e3e3e3;

    &__write {
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;

      input {
        box-sizing: border-box;
        border: none;
        border-radius: 3px;
        padding: 4px 8px;
        width: 80%;
        background-color: #e3e3e3;
      }
    }
    &__submit {
      max-width: 20%;
      button {
        box-sizing: border-box;
        border: none;
        border-radius: 3px;
        padding: 4px 8px;
        box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 2px,
          rgba(0, 0, 0, 0.07) 0px 2px 4px, rgba(0, 0, 0, 0.07) 0px 4px 8px,
          rgba(0, 0, 0, 0.07) 0px 8px 16px, rgba(0, 0, 0, 0.07) 0px 16px 32px,
          rgba(0, 0, 0, 0.07) 0px 32px 64px;
      }
    }

    .no-comments {
      text-align: center;
    }
  }
}
</style>
