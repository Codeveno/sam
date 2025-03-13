from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize DeepSORT tracker
tracker = DeepSort(model_path='models/ckpt.t7', max_age=30, n_init=3, nms_max_overlap=1.0)

def track_objects(detections, frame):
    """
    Tracks detected animals using DeepSORT.
    Returns tracked objects with IDs and bounding box data.
    """
    # Convert detections into DeepSORT's required format
    dets = [
        {
            "tlwh": (x1, y1, x2 - x1, y2 - y1),  # Format expected by DeepSORT
            "confidence": conf,
            "class": cls
        }
        for x1, y1, x2, y2, conf, cls in detections
    ]

    # DeepSORT expects frame in RGB format, ensure color format consistency
    if frame.shape[-1] == 3:  # Check if 3-channel (RGB)
        tracked_objects = tracker.update_tracks(dets, frame=frame)
    else:
        import cv2
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB if needed
        tracked_objects = tracker.update_tracks(dets, frame=rgb_frame)

    return tracked_objects
