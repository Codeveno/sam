import sys
import os
sys.path.append(os.path.join(os.getcwd(), "yolov5"))  # Ensure YOLOv5's utils is prioritized

import cv2
import threading
from utils.detection import detect_animals
from utils.tracking import track_objects
from utils.visualization import draw_tracks

# Dictionary for camera names and links
CAMERA_SOURCES = {
    "Nkorho Bush Lodge": "https://explore.org/livecams/african-wildlife/nkorho-bush-lodge",
    "Tembe Elephant Park": "https://explore.org/livecams/african-wildlife/tembe-elephant-park",
    "African Watering Hole": "https://explore.org/livecams/african-wildlife/african-watering-hole-animal-camera",
    "Lisbon Falls": "https://explore.org/livecams/african-wildlife/lisbon-falls",
    "HESC Cheetah Cam": "https://explore.org/livecams/african-wildlife/hesc-cheetah-cam-2",
    "Africam Show": "https://explore.org/livecams/african-wildlife/africam-shows",
    "Gorilla Forest Corridor": "https://explore.org/livecams/african-wildlife/gorilla-forest-corridor"
}

# Display options for camera selection
print("\n📷 Select a Camera to View:")
for i, cam in enumerate(CAMERA_SOURCES.keys(), 1):
    print(f"{i}. {cam}")

# Camera selection logic
try:
    choice = int(input("Enter the number of the camera you want to view: "))
    if choice < 1 or choice > len(CAMERA_SOURCES):
        raise ValueError("Invalid choice. Please select a valid camera number.")
except ValueError as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

selected_camera_name = list(CAMERA_SOURCES.keys())[choice - 1]
selected_camera_link = CAMERA_SOURCES[selected_camera_name]

# Process selected camera stream
def process_camera(source, window_name):
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

        # Visualize results
        frame = draw_tracks(frame, tracks)

        cv2.imshow(window_name, frame)

        # Press 'q' to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(f"✅ Closing {window_name}")
            break

    cap.release()
    cv2.destroyWindow(window_name)

# Start the selected camera feed in a separate thread
camera_thread = threading.Thread(target=process_camera, args=(selected_camera_link, selected_camera_name))
camera_thread.start()

# Ensure the main window closes cleanly
cv2.destroyAllWindows()
