<template>
  <div class="container">
    <div class="author">
      <div class="author__profile">
        <span class="img"><i class="fab fa-slideshare"></i></span>
        <div>
          <span>{{ postData.author }}</span>
          <span class="timestamp">{{ timestampToDate }}</span>
        </div>
      </div>
      <div class="action">
        <template v-if="isWritter">
          <button class="delete-post" @click="showDeleteModal = true">
            삭제하기
          </button>
        </template>
        <template v-else>
          <button class="recommend" @click="recommendPost">
            <span><i class="fas fa-thumbs-up"></i></span>
            {{ postData.recommend }}
          </button>
        </template>
      </div>
    </div>
    <div class="content">
      <div class="content__title">
        <span>{{ postData.title }}</span>
      </div>
      <div class="content__content">
        <p>
          {{ postData.content }}
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
    <DeleteModal
      v-if="showDeleteModal"
      @delete="deletePost"
      @cancel="showDeleteModal = false"
    />
  </div>
</template>

<script>
import CommentItem from '../../components/CommentItem.vue'
import DeleteModal from '../../components/DeleteModal.vue'

export default {
  components: { CommentItem, DeleteModal },
  async asyncData({ app, route }) {
    const postId = route.params.id
    const postData = await app.$fire.firestore
      .collection('post')
      .doc(postId)
      .get()
      .then((doc) => {
        return doc.data()
      })
    return { postData }
  },

  data() {
    return {
      isCommentExist: false,
      isRecommend: false,
      showDeleteModal: false,
    }
  },
  computed: {
    timestampToDate() {
      const timestamp = new Date(this.postData.created_at.seconds * 1000)
      const year = timestamp.getFullYear()
      const month = ('0' + (1 + timestamp.getMonth())).slice(-2)
      const day = ('0' + timestamp.getDate()).slice(-2)

      return year + '-' + month + '-' + day
    },
    isWritter() {
      if (this.postData.author_id === this.$store.getters.getUid) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    async recommendPost() {
      if (!this.isRecommend) {
        this.isRecommend = true
        await this.$fire.firestore
          .collection('post')
          .doc(this.$route.params.id)
          .update({ recommend: this.postData.recommend++ })
      } else {
        this.isRecommend = false
        await this.$fire.firestore
          .collection('post')
          .doc(this.$route.params.id)
          .update({ recommend: this.postData.recommend-- })
      }
    },
    deletePost() {
      this.showDeleteModal = false
    },
    handelCommentSubmit() {
      this.isCommentExist = true
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  height: $page-height;
  padding: 16px;

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
    .action {
      .recommend {
        background-color: transparent;
        font-size: $sub-heading;
        border: 1px solid $recommend;
        border-radius: 5px;
        padding: 8px 16px;
        color: $recommend;
      }

      .delete-post {
        background-color: transparent;
        font-size: $description;
        border: 1px solid #a83838;
        border-radius: 5px;
        padding: 8px;
        color: #a83838;
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

    .del-btn {
      display: flex;
      justify-content: flex-end;
      margin-top: 16px;

      button {
        border: 1px solid #a83838;
        border-radius: 5px;
        color: #a83838;
      }
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
