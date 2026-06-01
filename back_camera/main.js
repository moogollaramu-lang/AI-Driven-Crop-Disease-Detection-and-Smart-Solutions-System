function sendValue(value) {
  Streamlit.setComponentValue(value)
}

function onRender(event) {
  if (!window.rendered) {
    var { height, width } = event.detail.args;
    
    let video = document.getElementById('video');
    let canvas = document.getElementById('canvas');
    let captureBtn = document.getElementById('capture-btn');

    video.setAttribute('width', '100%');
    video.setAttribute('height', 'auto');
    
    // Request environment facing mode (rear camera)
    const constraints = { 
      video: {
        facingMode: 'environment',
        advanced : [{focusMode: "continuous"}]
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
      // Trigger shutter flash animation
      let flash = document.getElementById('flash-effect');
      if (flash) {
        flash.classList.remove('fade-out');
        flash.classList.add('flash');
        setTimeout(() => {
          flash.classList.remove('flash');
          flash.classList.add('fade-out');
        }, 50);
      }
      
      // Trigger temporary captured notification toast
      let status = document.getElementById('capture-status');
      if (status) {
        status.classList.add('show');
        setTimeout(() => {
          status.classList.remove('show');
        }, 2000);
      }

      let context = canvas.getContext('2d');
      // Capture at video native resolution for clarity
      const w = video.videoWidth || 640;
      const h = video.videoHeight || 480;
      canvas.width = w;
      canvas.height = h;
      context.drawImage(video, 0, 0, w, h);      
      var data = canvas.toDataURL('image/png');
      sendValue(data);
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
