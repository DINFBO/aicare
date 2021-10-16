<template>
  <div>
    감정분석 페이지
    <audio :src="diaryUrl" controls></audio>
  </div>
</template>
<script>
export default {
  props: {
    diaryUrl: {
      type: String,
      default() {
        return ''
      },
    },
  },
  data() {
    return {
      audio: null,
      playing: false,
    }
  },
  // methods: {
  //   play() {
  //     this.playing = true
  //     this.audio = new Audio(this.diaryUrl)
  //     this.audio.play()
  //   },
  //   pause() {
  //     this.playing = false
  //     this.audio.pause()
  //   },
  // },
}
</script>
<style lang="scss" scoped>
button {
  padding: 16px;
}
</style>
