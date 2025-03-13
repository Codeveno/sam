from flask import Flask, render_template, Response, request
import cv2
import threading
from eco_helpers.detection import detect_animals
from eco_helpers.tracking import track_objects
from eco_helpers.visualization import draw_tracks

app = Flask(__name__, template_folder='templates', static_folder='static')

# Corrected Camera Sources
CAMERA_SOURCES = {
    "Nkorho Bush Lodge": "https://youtu.be/dIChLG4_WNs",
    "Rosie Pan": "https://youtu.be/ItdXaWUVF48",
    "African Watering Hole": "https://youtu.be/KyQAB-TKOVA",
    "Lisbon Falls": "https://youtu.be/9viZIxuonrI",
    "HESC Cheetah Cam": "https://www.youtube.com/embed/luQSQuCHtcI",
    "Africam Show": "https://www.youtube.com/embed/a0BME_RcftQ",
    "Gorilla Forest Corridor": "https://youtu.be/yfSyjwY6zSQ"
}

# Stream generator function for live video feeds
def generate_frames(source):
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"❌ Failed to open camera source: {source}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"❌ Lost connection to {source}")
            break

        # Resize frame for performance improvement
        frame = cv2.resize(frame, (640, 480))

        # Detect animals using YOLOv5
        detections = detect_animals(frame)

        # Track animals using DeepSORT
        tracks = track_objects(detections, frame)

        # Visualize results with bounding boxes and labels
        frame = draw_tracks(frame, tracks)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Yield the frame as a byte stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

# Route to render `index.html`
@app.route('/')
def index():
    return render_template('index.html')

# Route for video feed display
@app.route('/video_feed/<camera_name>')
def video_feed(camera_name):
    source = CAMERA_SOURCES.get(camera_name)
    if not source:
        return "❌ Camera feed not available", 404

    # Handling YouTube live streams (embedded format)
    if "youtube" in source:
        return render_template('camera_feed.html', camera_name=camera_name, camera_url=source)
    
    # For direct camera links
    return Response(generate_frames(source),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
