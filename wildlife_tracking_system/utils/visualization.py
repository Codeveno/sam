import cv2

# Animal class names (customizable based on your dataset)
CLASS_NAMES = ['buffalo', 'elephant', 'rhino', 'zebra']

def draw_tracks(frame, tracks):
    """
    Draws bounding boxes and labels on the frame for tracked objects.
    """
    for track in tracks:
        if track.is_confirmed():
            track_id = track.track_id
            bbox = track.to_ltwh()
            x, y, w, h = map(int, bbox)

            label = CLASS_NAMES[track.det_class] if track.det_class < len(CLASS_NAMES) else "Unknown"
            color = (0, 255, 0)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} ID:{track_id}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame
