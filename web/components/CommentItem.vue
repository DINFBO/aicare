<template>
  <div class="comment">
    <div class="comment__profile">
      <div class="author">
        <img src="" alt="" />
        <span>{{ data.author }}</span>
      </div>
      <span class="timestamp"> {{ timestampToDate }} </span>
    </div>
    <div class="comment__content">
      <span>{{ data.comment_content }}</span>
      <template v-if="isCommentWritter">
        <button @click="showDeleteModal = true">
          <i class="far fa-trash-alt"></i>
        </button>
      </template>
    </div>
    <DeleteModal
      v-if="showDeleteModal"
      @delete="deleteComment"
      @cancel="showDeleteModal = false"
    />
  </div>
</template>

<script>
import DeleteModal from './DeleteModal.vue'
export default {
  components: { DeleteModal },
  props: {
    data: {
      type: Object,
      default() {
        return {}
      },
    },
    id: {
      type: String,
      default() {
        return ''
      },
    },
  },
  data() {
    return {
      showDeleteModal: false,
    }
  },
  computed: {
    timestampToDate() {
      const timestamp = new Date(this.data.created_at.seconds * 1000)
      const year = timestamp.getFullYear()
      const month = ('0' + (1 + timestamp.getMonth())).slice(-2)
      const day = ('0' + timestamp.getDate()).slice(-2)

      return year + '-' + month + '-' + day
    },
    isCommentWritter() {
      if (this.data.author === this.$store.getters.getUsername) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    async deleteComment() {
      await this.$fire.firestore
        .collection('post')
        .doc(this.$route.params.id)
        .collection('comment')
        .doc(this.id)
        .delete()
        .then(() => {
          this.$nuxt.refresh()
          this.showDeleteModal = false
        })
        .catch((err) => console.log(err))
    },
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
      background-color: transparent;
      font-size: 16px;
      color: #a83838;
    }
  }
}
</style>
