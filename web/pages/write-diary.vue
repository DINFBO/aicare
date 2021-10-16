<template>
  <div class="container">
    <div class="feedback">일기를 작성해주시면 분석결과가 나타납니다.</div>
    <div class="record">
      <button v-if="!isRecording" class="start-btn" @click="startRecording">
        녹음 시작
      </button>
      <button v-else class="stop-btn" @click="stopRecording">녹음 종료</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recorder: null,
      chunks: [],
      downloadURL: '',
      isRecording: false,
    }
  },
  computed: {
    timeToDate() {
      const time = new Date()
      const year = time.getFullYear()
      const month = ('0' + (1 + time.getMonth())).slice(-2)
      const day = ('0' + time.getDate()).slice(-2)

      return year + '-' + month + '-' + day
    },
  },
  methods: {
    startRecording() {
      const contraint = { audio: true, video: false }
      navigator.mediaDevices
        .getUserMedia(contraint)
        .then(this.handleSuccess)
        .catch((e) => {
          console.log(e)
        })
    },
    handleSuccess(stream) {
      this.isRecording = true
      this.recorder = new MediaRecorder(stream)
      this.recorder.start()
      this.recorder.ondataavailable = (e) => {
        this.chunks.push(e.data)
      }
      this.recorder.onstop = (e) => {
        const blob = new Blob(this.chunks, { type: 'audio/ogg; codecs=opus' })
        this.chunks = []
        this.saveAudio(blob)
        this.recorder = null
      }
    },
    stopRecording() {
      this.isRecording = false
      this.diaryName = ''
      this.recorder.stop()
    },
    async saveAudio(blob) {
      const uid = await this.$store.getters.getUid
      const currentDate = await this.timeToDate
      const diaryRef = await this.$fire.storage.ref(
        `${uid}/diary/${currentDate}`
      )
      diaryRef.put(blob)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  height: $page-height;
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;

  .feedback {
    height: 55vh;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid $gray;
    border-radius: 10px;
  }

  .record {
    box-sizing: border-box;
    background-color: $yellow-light;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    max-height: 12vh;
    padding: 16px 0;
    min-height: 120px;
    padding: 8px 0;
    border-radius: 5px;

    input {
      border: none;
      padding: 8px 16px;
      font-size: 16px;
      width: 70%;
    }

    button {
      border: none;
      padding: 8px 20px;
      font-size: 18px;
      background-color: transparent;
      border-radius: 5px;
    }

    .start-btn {
      color: $success;
      border: 1px solid $success;
    }

    .stop-btn {
      background-color: $fail;
    }
  }
}
</style>
