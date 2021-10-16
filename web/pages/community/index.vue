<template>
  <div class="container">
    <div class="title">
      <span>감정을 공유해보세요</span>
      <nuxt-link class="write" to="/community/write">글 쓰기</nuxt-link>
    </div>
    <PostItem v-for="post in posts" :key="post.id" :data="post.data" @click.native="goPostDetail(post.id)"/>
  </div>
</template>

<script>
import PostItem from '../../components/PostItem.vue'
export default {
  components: { PostItem },
  async asyncData({ app }) {
    const posts = await app.$fire.firestore
      .collection('post')
      .orderBy('created_at')
      .get()
      .then((querySnapshot) => {
        const result = []
        querySnapshot.forEach((doc) => {
          result.push({ id: doc.id, data: doc.data() })
        })
        return result.slice().reverse()
      })
    return { posts }
  },
  methods: {
    goPostDetail(id) {
      this.$router.push(`community/${id}`)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  height: $page-height;
  padding: 16px;

  .title {
    padding-top: 16px;
    margin-bottom: 36px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    span {
      font-size: $heading;
      font-weight: bold;
      word-break: keep-all;
      line-height: 1.2;
    }

    .write {
      padding: 8px;
      max-height: 30px;
      border: 1px solid $gray;
      color: $white;
      border-radius: 5px;
      font-size: $sub-heading;

      text-decoration: none;
      color: $gray;
    }
  }
}
</style>
