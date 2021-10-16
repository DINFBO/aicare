<template>
  <div class="container">
    <div class="user">
      <span class="user__title">안녕하세요 {{ user.name }}님!</span>
      <span class="user__subtitle"
        >전역까지 {{ dischargeDay }}일 남았습니다.</span
      >
      <div class="user__img">
        <img :src="profileImg" alt="" />
      </div>
    </div>
    <div class="main">
      <div class="hits-posts">
        <div class="title title--bold">
          <span>인기글</span>
        </div>
        <ul>
          <li v-for="post in posts" :key="post.id" @click="$router.push(`community/${post.id}`)">
            <span class="hits-posts__title">{{ post.title }}</span>
            <span class="hits-posts__timestamp">{{
              timestampToDate(post.timestamp)
            }}</span>
          </li>
        </ul>
      </div>
      <div class="goto" @click="$router.push('/write-diary')">
        <span>오늘은 어떤 일이 있으셨나요?</span>
        <span>일기 쓰러 가기</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  async asyncData({ app, store }) {
    const uid = await store.getters.getUid
    const snapshot = app.$fire.firestore.collection('user').doc(uid)
    const pathReference = await app.$fire.storage.ref(`${uid}/profile/`)
    const user = await snapshot.get().then((doc) => {
      if (doc.exists) {
        return doc.data()
      }
    })
    const profileImg = await pathReference.listAll().then((result) => {
      const imgUrl = result.items[0].getDownloadURL().then((url) => {
        return url
      })

      return imgUrl
    })
    store.dispatch('setUserName', user.name)

    const posts = await app.$fire.firestore
      .collection('post')
      .orderBy('recommend', 'desc')
      .limit(3)
      .get()
      .then((querySnapshot) => {
        const result = []
        querySnapshot.forEach((doc) => {
          const data = doc.data()
          result.push({
            id: doc.id,
            title: data.title,
            timestamp: data.created_at,
          })
        })
        return result
      })
    return { user, profileImg, posts }
  },
  data() {
    return {}
  },
  computed: {
    dischargeDay() {
      const today = new Date()
      const dischargeDate = new Date(this.user.discharge_date)
      const gap = dischargeDate.getTime() - today.getTime()
      const result = Math.ceil(gap / (1000 * 60 * 60 * 24))
      return result
    },
  },
  methods: {
    timestampToDate(createdAt) {
      const timestamp = new Date(createdAt.seconds * 1000)
      const now = new Date()
      const yesterday = new Date(now.setDate(now.getDate() - 1))
      if (yesterday <= timestamp) {
        let hour = timestamp.getHours()
        hour = hour >= 10 ? hour : '0' + hour
        const min = timestamp.getMinutes()
        return `${hour}:${min}`
      } else {
        const year = timestamp.getFullYear()
        const month = ('0' + (1 + timestamp.getMonth())).slice(-2)
        const day = ('0' + timestamp.getDate()).slice(-2)
        return `${year}-${month}-${day}`
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  padding: 32px 16px;
  height: $page-height;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  .title {
    font-size: $sub-heading;

    &--bold {
      font-weight: bold;
      color: #e6c823;
    }
  }

  .user {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    &__title {
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 10px !important;
    }
    &__subtitle {
      font-size: 14px;
    }
    &__img {
      display: flex;
      justify-content: center;
      margin: 24px 0 !important;

      img {
        width: 170px;
        height: 170px;
        border-radius: 50%;
        background-color: #e6c823;
      }
    }
  }

  .main {
    height: 35vh;
    min-height: 250px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;

    .hits-posts {
      width: 100%;
      box-sizing: border-box !important;
      padding: 12px 16px;
      box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px,
        rgba(0, 0, 0, 0.24) 0px 1px 2px;
      border-radius: 5px;

      ul {
        li {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin: 12px 0 !important;
          cursor: pointer;
        }
      }

      &__timestamp {
        font-size: 12px;
        color: #939597;
      }
    }

    .goto {
      width: 100%;
      padding: 24px 0;
      background-color: $yellow-light;
      box-sizing: border-box !important;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      line-height: 1.5;
      cursor: pointer;

      span:last-child {
        font-weight: bold;
      }
    }
  }
}
</style>
