// Handle camera selection and navigation
function selectCamera(cameraName) {
    const cameraURL = getCameraURL(cameraName);

    if (cameraURL) {
        localStorage.setItem('selectedCameraURL', cameraURL);
        localStorage.setItem('selectedCameraName', cameraName);

        // Redirect to correct feed handling page
        if (cameraURL.includes("youtube")) {
            window.location.href = '/camera_feed'; // Corrected URL
        } else {
            window.location.href = `/video_feed/${encodeURIComponent(cameraName)}`;
        }
    } else {
        alert('❌ Camera feed not available.');
    }
}

// Display the selected camera feed
window.onload = function () {
    const cameraFeedElement = document.getElementById('camera-feed-container'); // Corrected ID
    const cameraTitleElement = document.getElementById('camera-title');
    const selectedCameraURL = localStorage.getItem('selectedCameraURL');
    const selectedCameraName = localStorage.getItem('selectedCameraName');

    if (cameraFeedElement && selectedCameraURL) {
        if (selectedCameraURL.includes("youtube")) {
            // Embed YouTube stream
            cameraFeedElement.innerHTML = `
                <iframe 
                    src="${selectedCameraURL}" 
                    width="100%" 
                    height="500px" 
                    frameborder="0" 
                    allowfullscreen>
                </iframe>`;
        } else {
            // Direct video feed (handled by Flask route)
            cameraFeedElement.innerHTML = `
                <img src="${selectedCameraURL}" alt="${selectedCameraName}" width="100%" height="500px">`;
        }

        cameraTitleElement.textContent = selectedCameraName;
    } else {
        cameraTitleElement.textContent = '❌ Camera Feed Not Available';
    }
}

// Dictionary of actual camera links
function getCameraURL(cameraName) {
    const cameraFeeds = {
        "Nkorho Bush Lodge": "https://www.youtube.com/embed/dIChLG4_WNs",
        "Rosie Pan": "https://www.youtube.com/embed/ItdXaWUVF48",
        "African Watering Hole": "https://www.youtube.com/embed/KyQAB-TKOVA",
        "Lisbon Falls": "https://www.youtube.com/embed/9viZIxuonrI",
        "HESC Cheetah Cam": "https://www.youtube.com/embed/luQSQuCHtcI",
        "Africam Show": "https://www.youtube.com/embed/a0BME_RcftQ",
        "Gorilla Forest Corridor": "https://www.youtube.com/embed/yfSyjwY6zSQ"
    };
    return cameraFeeds[cameraName] || null;
}
