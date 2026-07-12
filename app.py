from ultralytics import YOLO
import cv2
import numpy as np

# Load lightweight YOLO model
model = YOLO("yolov8n.pt")

# Camera video paths
video_paths = [
    "videos/camera1.mp4",
    "videos/camera2.mp4",
    "videos/camera3.mp4",
    "videos/camera4.mp4"
]

# Camera locations
CAMERA_LOCATIONS = {
    1: "Main Entrance",
    2: "Public Walkway",
    3: "Restricted Laboratory",
    4: "Staff Entrance"
}

# Open all camera videos
caps = [cv2.VideoCapture(path) for path in video_paths]

# Display resolution
DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 360

# Smaller resolution for faster AI detection
DETECT_WIDTH = 320
DETECT_HEIGHT = 180

# Restricted-zone positions
BOTTOM_LINE = 265
TOP_LINE = 125

# Run YOLO once every 5 frames
DETECT_EVERY = 5
frame_count = 0

# Store previous person detections
cached_boxes = [[], [], [], []]


def get_person_boxes(result):
    boxes_list = []

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        # YOLO class 0 means person
        if class_id == 0 and confidence >= 0.35:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Convert detection coordinates to display coordinates
            scale_x = DISPLAY_WIDTH / DETECT_WIDTH
            scale_y = DISPLAY_HEIGHT / DETECT_HEIGHT

            x1 = int(x1 * scale_x)
            y1 = int(y1 * scale_y)
            x2 = int(x2 * scale_x)
            y2 = int(y2 * scale_y)

            boxes_list.append((x1, y1, x2, y2))

    return boxes_list


def process_camera(frame, camera_number, boxes):
    output = frame.copy()
    intrusion = False

    for x1, y1, x2, y2 in boxes:
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        foot_y = y2

        inside_zone = False

        # Camera 1 and Camera 2:
        # Bottom part is restricted
        if camera_number in [1, 2]:
            inside_zone = foot_y > BOTTOM_LINE

        # Camera 3:
        # Entire frame is restricted
        elif camera_number == 3:
            inside_zone = True

        # Camera 4:
        # Top part is restricted
        elif camera_number == 4:
            inside_zone = center_y < TOP_LINE

        # Box color and label
        if inside_zone:
            color = (0, 0, 255)       # Red
            label = "INTRUDER"
            intrusion = True
        else:
            color = (0, 255, 0)       # Green
            label = "PERSON"

        # Draw person box
        cv2.rectangle(
            output,
            (x1, y1),
            (x2, y2),
            color,
            2
        )

        # Draw person label
        cv2.putText(
            output,
            label,
            (x1, max(y1 - 8, 25)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

        # Draw checking point
        point_y = foot_y if camera_number in [1, 2] else center_y

        cv2.circle(
            output,
            (center_x, point_y),
            5,
            color,
            -1
        )

    # Camera 1 and Camera 2 restricted zone
    if camera_number in [1, 2]:
        cv2.line(
            output,
            (0, BOTTOM_LINE),
            (DISPLAY_WIDTH, BOTTOM_LINE),
            (0, 0, 255),
            3
        )

        cv2.putText(
            output,
            "BOTTOM RESTRICTED ZONE",
            (12, BOTTOM_LINE + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    # Camera 3 full-frame restricted zone
    elif camera_number == 3:
        cv2.rectangle(
            output,
            (3, 3),
            (DISPLAY_WIDTH - 3, DISPLAY_HEIGHT - 3),
            (0, 0, 255),
            4
        )

        cv2.putText(
            output,
            "FULL FRAME RESTRICTED",
            (170, DISPLAY_HEIGHT - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    # Camera 4 top restricted zone
    elif camera_number == 4:
        cv2.line(
            output,
            (0, TOP_LINE),
            (DISPLAY_WIDTH, TOP_LINE),
            (0, 0, 255),
            3
        )

        cv2.putText(
            output,
            "TOP RESTRICTED ZONE",
            (12, TOP_LINE - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    # White background for camera title and location
    cv2.rectangle(
        output,
        (5, 5),
        (340, 78),
        (255, 255, 255),
        -1
    )

    # Camera title in black
    cv2.putText(
        output,
        f"Camera {camera_number}",
        (15, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.85,
        (0, 0, 0),
        2
    )

    # Camera location in black
    cv2.putText(
        output,
        CAMERA_LOCATIONS[camera_number],
        (15, 63),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.62,
        (0, 0, 0),
        2
    )

    # Camera status
    if intrusion:
        status = "ALERT"
        status_color = (0, 0, 255)
    else:
        status = "SAFE"
        status_color = (0, 255, 0)

    cv2.putText(
        output,
        status,
        (DISPLAY_WIDTH - 120, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        status_color,
        2
    )

    return output, intrusion


# Create output window
cv2.namedWindow(
    "EyeWitness AI - Four Camera Monitoring",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "EyeWitness AI - Four Camera Monitoring",
    1300,
    800
)

while True:
    display_frames = []
    detection_frames = []

    # Read frames from all four cameras
    for cap in caps:
        success, frame = cap.read()

        # Restart video when finished
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, frame = cap.read()

        # Black screen if video cannot be opened
        if not success:
            display_frame = np.zeros(
                (DISPLAY_HEIGHT, DISPLAY_WIDTH, 3),
                dtype=np.uint8
            )
        else:
            display_frame = cv2.resize(
                frame,
                (DISPLAY_WIDTH, DISPLAY_HEIGHT)
            )

        detection_frame = cv2.resize(
            display_frame,
            (DETECT_WIDTH, DETECT_HEIGHT)
        )

        display_frames.append(display_frame)
        detection_frames.append(detection_frame)

    frame_count += 1

    # Run detection only every few frames
    if frame_count % DETECT_EVERY == 0:
        results = model(
            detection_frames,
            imgsz=320,
            conf=0.35,
            verbose=False
        )

        for i, result in enumerate(results):
            cached_boxes[i] = get_person_boxes(result)

    outputs = []
    alerts = []

    # Process all four cameras
    for i in range(4):
        camera_number = i + 1

        output, alert = process_camera(
            display_frames[i],
            camera_number,
            cached_boxes[i]
        )

        outputs.append(output)
        alerts.append(alert)

    # Arrange cameras in 2 x 2 grid
    top_row = np.hstack((outputs[0], outputs[1]))
    bottom_row = np.hstack((outputs[2], outputs[3]))
    camera_grid = np.vstack((top_row, bottom_row))

    # Build alert message with camera number and location
    alert_messages = []

    for i, alert in enumerate(alerts):
        if alert:
            camera_number = i + 1
            location = CAMERA_LOCATIONS[camera_number]

            alert_messages.append(
                f"CAM {camera_number} - {location}"
            )

    if alert_messages:
        message = "ALERT: " + " | ".join(alert_messages)
        message_color = (0, 0, 255)
    else:
        message = "ALL CAMERAS SAFE"
        message_color = (0, 255, 0)

    # Create black alert banner
    banner = np.zeros(
        (60, DISPLAY_WIDTH * 2, 3),
        dtype=np.uint8
    )

    # Reduce text size when many alerts appear
    banner_font_scale = 0.85 if len(message) > 45 else 1.05
    banner_thickness = 2

    text_size = cv2.getTextSize(
        message,
        cv2.FONT_HERSHEY_SIMPLEX,
        banner_font_scale,
        banner_thickness
    )[0]

    text_x = max(
        10,
        ((DISPLAY_WIDTH * 2) - text_size[0]) // 2
    )

    cv2.putText(
        banner,
        message,
        (text_x, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        banner_font_scale,
        message_color,
        banner_thickness
    )

    # Add banner above camera grid
    final_output = np.vstack((banner, camera_grid))

    # Show output
    cv2.imshow(
        "EyeWitness AI - Four Camera Monitoring",
        final_output
    )

    # Press q to close
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Release all videos
for cap in caps:
    cap.release()

cv2.destroyAllWindows()