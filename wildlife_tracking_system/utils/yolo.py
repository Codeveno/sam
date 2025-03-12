from ultralytics import YOLO

# Load YOLOv5 model
def load_yolo_model():
    return YOLO('models/best.pt')
