function sendValue(value) {
  Streamlit.setComponentValue(value)
}

function onRender(event) {
  if (!window.rendered) {
    var { height, width, facingMode } = event.detail.args;
    
    let video = document.getElementById('video');
    let canvas = document.getElementById('canvas');
    let captureBtn = document.getElementById('capture-btn');

    video.setAttribute('width', '100%');
    video.setAttribute('height', 'auto');
    
    // Request specified facing mode (default to environment/rear camera)
    const userFacingMode = facingMode || 'environment';
    const constraints = { 
      video: {
        facingMode: userFacingMode,
        ...(userFacingMode === 'environment' ? { advanced : [{focusMode: "continuous"}] } : {})
      }
    };
    
    navigator.mediaDevices.getUserMedia(constraints)
      .then(function(stream) {
        video.srcObject = stream;
        video.play();
      })
      .catch(function(err) {
        console.log("An error occurred: " + err);
      });

    function takePicture() {
      let context = canvas.getContext('2d');
      // Capture at video native resolution for clarity
      const w = video.videoWidth || 640;
      const h = video.videoHeight || 480;
      canvas.width = w;
      canvas.height = h;
      context.drawImage(video, 0, 0, w, h);      
      var data = canvas.toDataURL('image/png');
      
      // Instantly render preview inside WebRTC component
      let previewImg = document.getElementById('preview');
      previewImg.src = data;
      previewImg.style.display = 'block';
      video.style.display = 'none';
      captureBtn.style.display = 'none';
      
      sendValue(data);

      // Stop all tracks on the active media stream to turn off the camera immediately!
      if (video.srcObject) {
        const stream = video.srcObject;
        stream.getTracks().forEach(track => track.stop());
        video.srcObject = null;
      }
    }      

    // Adjust container frame height dynamically
    Streamlit.setFrameHeight(height + 65);

    // Trigger photo capture on both button and video clicks
    captureBtn.addEventListener('click', takePicture);
    video.addEventListener('click', takePicture);
    
    window.rendered = true
  }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
