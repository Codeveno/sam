from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize DeepSORT tracker
tracker = DeepSort(model_path='models/ckpt.t7', max_age=30, n_init=3, nms_max_overlap=1.0)

def track_objects(detections, frame):
    """
    Tracks detected animals using DeepSORT.
    Returns tracked objects with IDs and bounding box data.
    """
    tracked_objects = tracker.update_tracks(detections, frame=frame)
    return tracked_objects
