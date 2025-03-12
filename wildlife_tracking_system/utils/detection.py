from utils.yolo import load_yolo_model

# Load YOLOv5 model
model = load_yolo_model()

def detect_animals(frame):
    """
    Detect animals using YOLOv5.
    Returns a list of detections: [(x1, y1, x2, y2, confidence, class_id), ...]
    """
    results = model.predict(frame)
    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            if conf > 0.5:
                detections.append((x1, y1, x2, y2, conf, cls))

    return detections
