<template>
  <div>
    <button ref="startBtn" @click="startRecording">녹음시작</button>
    <button ref="stopBtn" @click="stopRecording">정지</button>
    <div>{{ data }}</div>
    <ul>
      <li v-for="record in result" :key="record.url">
        {{ record.name }}<br />
        {{ record.url }}
        <audio ref="player" controls>
          <source :src="record.url" type="audio/webm" />
        </audio>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      player: this.$refs.player,
      chunks: [],
      // audioCtx: null,
      // analyser: null,
      recorder: null,
      data: null,
      result: [],
    }
  },
  // mounted() {
  //   this.audioCtx = new (window.AudioContext || window.webkitAudioContext)()
  //   this.analyser = this.audioCtx.createAnalyser()
  // },

  methods: {
    // makeSound(stream) {
    //   const source = this.audioCtx.createMediaStreamSource(stream)
    //   source.connect(this.analyser)
    //   this.analyser.connect(this.audioCtx.destination)
    // },
    startRecording() {
      const device = navigator.mediaDevices.getUserMedia({ audio: true })
      device.then((stream) => {
        this.recorder = new MediaRecorder(stream)
        // this.audioCtx.resume()
        // this.makeSound(stream)

        this.recorder.start()
        this.data = this.recorder.state
        alert('start recording')
      })
    },
    async stopRecording() {
      this.recorder.ondataavailable = (e) => {
        if (e.data.size > 0) this.chunks.push(e.data)
      }
      await this.recorder.stop()
      this.data = this.recorder.state
      alert('stop recording')
      this.save()
    },

    save() {
      const blob = new Blob(this.chunks, {
        mimeType: 'audio/webm;codecs=opus',
      })
      this.chunks = []
      const audioURL = URL.createObjectURL(blob)
      this.result.push({
        name: new Date(),
        url: audioURL,
      })

      // const formdata = new FormData()
      // formdata.append('fname', `${new Date('yyyy-mm-dd')}.webm`)
      // formdata.append('data', blob)
      // console.log(formdata)

      // const xhr = new XMLHttpRequest()
      // xhr.open('POST', '/upload', false)
      // xhr.send(formdata)
      // alert('recorder stopped')
    },
  },
}
</script>
