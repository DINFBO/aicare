export const record = () => {
  if (navigator.mediaDevices) {
    console.log('getUserMedia supported.')

    const constraints = { audio: true }
    // let chunks = []

    navigator.mediaDevices
      .getUserMedia(constraints)
      .then(function (stream) {
        const mediaRecorder = new MediaRecorder(stream)
        console.log(mediaRecorder)
        // record.onclick = function() {
        //   mediaRecorder.start();
        //   console.log(mediaRecorder.state);
        //   console.log("recorder started");
        //   record.style.background = "red";
        //   record.style.color = "black";
        // }

        // stop.onclick = function() {
        //   mediaRecorder.stop();
        //   console.log(mediaRecorder.state);
        //   console.log("recorder stopped");
        //   record.style.background = "";
        //   record.style.color = "";
        // }

        // mediaRecorder.onstop = function (e) {}

        // mediaRecorder.ondataavailable = function (e) {
        //   chunks.push(e.data)
        // }
      })
      .catch(function (err) {
        console.log('The following error occurred: ' + err)
      })
  }
}
