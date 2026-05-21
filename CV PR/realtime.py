import cv2
import mediapipe as mp

from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core.base_options import BaseOptions

base_options = BaseOptions(model_asset_path="face_landmarker.task")

options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_faces=1
)

detector = vision.FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
frame_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect_for_video(mp_image, frame_id)
    frame_id += 1

    if result.face_landmarks:
        for face_landmarks in result.face_landmarks:
            for lm in face_landmarks:
                h, w, _ = frame.shape
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                # cv2.rectangle(frame, (x-2, y-2), (x+2, y+2), (0, 255, 0), -1)

    cv2.imshow("Face Landmarks", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()