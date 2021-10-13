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
          <li>
            <span class="hits-posts__title">오늘은 힘든 날이다...</span>
            <span class="hits-posts__timestamp">09/26 22:58</span>
          </li>
          <li>
            <span class="hits-posts__title">오늘은 힘든 날이다...</span>
            <span class="hits-posts__timestamp">09/26 22:58</span>
          </li>
          <li>
            <span class="hits-posts__title">오늘은 힘든 날이다...</span>
            <span class="hits-posts__timestamp">09/26 22:58</span>
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
  async asyncData({ app, store, error }) {
    const uid = await store.getters.getUid
    const snapshot = app.$fire.firestore.collection('user').doc(uid).get()
    const pathReference = app.$fire.storage.ref(`${uid}/profile/`)
    const user = await snapshot.then((doc) => {
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
    return { user, profileImg }
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
      margin-top: 48px !important;

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
