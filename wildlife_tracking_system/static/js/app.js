// Handle camera selection and navigation
function selectCamera(cameraName) {
    const cameraURL = getCameraURL(cameraName);
    if (cameraURL) {
        localStorage.setItem('selectedCameraURL', cameraURL);
        localStorage.setItem('selectedCameraName', cameraName);
        window.location.href = 'camera_feed.html';
    } else {
        alert('❌ Camera feed not available.');
    }
}

// Display the selected camera feed
window.onload = function () {
    const cameraFeedElement = document.getElementById('camera-feed');
    const cameraTitleElement = document.getElementById('camera-title');
    const selectedCameraURL = localStorage.getItem('selectedCameraURL');
    const selectedCameraName = localStorage.getItem('selectedCameraName');

    if (cameraFeedElement && selectedCameraURL) {
        cameraFeedElement.src = selectedCameraURL;
        cameraTitleElement.textContent = selectedCameraName;
    } else {
        cameraTitleElement.textContent = '❌ Camera Feed Not Available';
    }
}

// Dictionary of actual camera links
function getCameraURL(cameraName) {
    const cameraFeeds = {
        "Nkorho Bush Lodge": "https://www.youtube.com/embed/qkjBW_1Mf_k",
        "Tembe Elephant Park": "https://www.youtube.com/embed/qH5zR_eJvTo",
        "African Watering Hole": "https://www.youtube.com/embed/NqSFTWgXK4A",
        "Lisbon Falls": "https://www.youtube.com/embed/xh6R_t3OkAk",
        "HESC Cheetah Cam": "https://www.youtube.com/embed/luQSQuCHtcI",
        "Africam Show": "https://www.youtube.com/embed/a0BME_RcftQ",
        "Gorilla Forest Corridor": "https://www.youtube.com/embed/fp1B2nFo7lA"
    };
    return cameraFeeds[cameraName] || null;
}
