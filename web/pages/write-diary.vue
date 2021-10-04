<template>
  <div class="container">
    <div class="feedback"></div>
    <div class="record">
      <input
        v-model="diaryName"
        type="text"
        placeholder="일기 제목을 입력해주세요"
      />
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
      diaryName: '',
      downloadURL: '',
      isRecording: false,
    }
  },
  methods: {
    startRecording() {
      this.isRecording = true
      const contraint = { audio: true, video: false }
      navigator.mediaDevices
        .getUserMedia(contraint)
        .then(this.handleSuccess)
        .catch()
    },
    handleSuccess(stream) {
      this.recorder = new MediaRecorder(stream)
      this.recorder.start()
      console.log(this.recorder.state)
      this.recorder.ondataavailable = (e) => {
        console.log('data available')
        this.chunks.push(e.data)
      }
      this.recorder.onstop = (e) => {
        console.log('recorder stopped')

        const blob = new Blob(this.chunks, { type: 'audio/ogg; codecs=opus' })
        this.chunks = []
        const audioURL = window.URL.createObjectURL(blob)
        console.log(audioURL)
        this.downloadURL = audioURL
      }
    },
    stopRecording() {
      this.isRecording = false
      this.recorder.stop()
      console.log(this.recorder.state)
    },
  },
}
</script>
<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: $page-height;
  padding: 16px;

  .record {
    background-color: #f9f0af;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    height: 100px;
    padding: 16px 0;

    input {
      border: none;
      padding: 8px 16px;
      font-size: 16px;
    }

    button {
      border: none;
      padding: 8px 20px;
      font-size: 18px;
      font-weight: bold;
      color: #ffffff;
      border-radius: 5px;
    }

    .start-btn {
      background-color: rgb(45, 172, 45);
    }

    .stop-btn {
      background-color: red;
    }
  }
}
</style>
