<template>
  <div class="container">
    <div class="title">
      <span>감정을 공유해보세요</span>
    </div>
    <div class="write">
      <nuxt-link to="/community/write">작성하기</nuxt-link>
    </div>
    <PostItem v-for="i in 10" :key="i" @click.native="goPostDetail(i)"/>
  </div>
</template>
<script>
import PostItem from '../../components/PostItem.vue'
export default {
  components: { PostItem },
  methods: {
    goPostDetail(id) {
      this.$router.push(`community/${id}`)
    }
  },
}
</script>
<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: $page-height;
  padding: 16px;
  overflow-y: scroll;
  position: relative;

  .title {
    font-size: $heading;
    font-weight: bold;
    padding-top: 16px;
    margin-bottom: 36px;
  }

  .write {
    padding: 8px 16px;
    background-color: $yellow;
    position: absolute;
    top: 32px;
    right: 16px;
    border-radius: 5px;
    a {
      text-decoration: none;
      color: $gray;
    }
  }
}
</style>
