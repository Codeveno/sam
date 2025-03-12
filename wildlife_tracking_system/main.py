import cv2
from utils.detection import detect_animals
from utils.tracking import track_objects
from utils.visualization import draw_tracks

# Video source (0 = webcam, or provide video file path)
VIDEO_SOURCE = 0  

def main():
    cap = cv2.VideoCapture(VIDEO_SOURCE)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect animals using YOLOv5
        detections = detect_animals(frame)

        # Track animals using DeepSORT
        tracks = track_objects(detections, frame)

        # Visualize results
        frame = draw_tracks(frame, tracks)

        cv2.imshow('Wildlife Tracking System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
