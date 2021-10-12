<template>
  <div class="post">
    <div>
      <div class="post__title">
        <span>{{ data.title }}</span>
      </div>
      <div class="post__create">
        <div class="post__author">
          <span class="author-img"><i class="far fa-user"></i></span>
          <span>{{ data.author_name }}</span>
        </div>
        <div class="post__timestamp">{{ timestampToDate }}</div>
      </div>
    </div>
    <button class="post__recommend">
      <span><i class="fas fa-thumbs-up"></i></span>
      {{ data.recommend }}
    </button>
  </div>
</template>
<script>
export default {
  props: {
    data: {
      type: Object,
      default() {
        return {}
      },
    },
  },
  computed: {
    timestampToDate() {
      const timestamp = new Date(this.data.created_at.seconds * 1000)
      const year = timestamp.getFullYear()
      const month = ('0' + (1 + timestamp.getMonth())).slice(-2)
      const day = ('0' + timestamp.getDate()).slice(-2)

      return year + '-' + month + '-' + day
    },
  },
}
</script>
<style lang="scss" scoped>
.post {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  min-height: 50px;
  margin: 24px 0;
  cursor: pointer;

  div:first-child {
    flex: 1;
  }
  &__title {
    font-size: $sub-heading;
    font-weight: bold;
    margin-bottom: 8px;
  }
  &__create {
    display: flex;
    justify-content: space-between;
    font-size: 16px;
  }
  &__timestamp {
    font-size: $description;
  }
  &__author {
    display: flex;
    align-items: center;
    .author-img {
      font-size: 14px;
      margin-right: 6px;
    }
  }

  &__recommend {
    box-sizing: border-box;
    width: 50px;
    padding: 4px 6px;
    margin-left: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: $description;
    font-weight: bold;
    color: $recommend;
    border: 1px solid $recommend;
    border-radius: 3px;

    span:first-child {
      margin-right: 5px;
    }
  }
}
</style>
