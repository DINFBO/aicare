<template>
  <div>
    <EmotionalAnalysis :diary-url="diaryUrl" />
  </div>
</template>
<script>
import EmotionalAnalysis from '../../components/EmotionalAnalysis.vue'
export default {
  components: { EmotionalAnalysis },
  async asyncData({ app, store, route }) {
    const date = route.params.date
    const uid = store.getters.getUid
    const diaryRef = await app.$fire.storage.ref(`${uid}/diary/${date}`)
    const diaryUrl = await diaryRef.getDownloadURL().then((url) => {
      return url
    })

    return { diaryUrl }
  },
}
</script>
<style lang="scss" scoped></style>
