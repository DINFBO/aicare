<template>
  <div class="container">
    <div class="feedback">일기를 작성해주시면 분석결과가 나타납니다.</div>
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
      this.diaryName = ''
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
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;

  .feedback {
    height: 55vh;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 10px;
    background-color: #D5D5D8;
  }

  .record {
    background-color: #f9f0af;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    max-height: 12vh;
    min-height: 11vh;
    padding: 16px 0;

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
      color: #ffffff;
      border-radius: 5px;
    }

    .start-btn {
      background-color: #6B9368;
    }

    .stop-btn {
      background-color: #B65A5A;
    }
  }
}
</style>
