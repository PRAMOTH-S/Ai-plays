import cv2
import numpy as np
import mediapipe as mp
from collections import deque

# -------------------------------
# 1. Initialize MediaPipe
# -------------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# -------------------------------
# 2. Canvas Setup
# -------------------------------
paint_window = np.zeros((480, 640, 3)) + 255

# Color points storage
blue_points = [deque(maxlen=1024)]
green_points = [deque(maxlen=1024)]
red_points = [deque(maxlen=1024)]
yellow_points = [deque(maxlen=1024)]

blue_index = green_index = red_index = yellow_index = 0

# Colors (BGR)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color_index = 0

# -------------------------------
# 3. UI Buttons
# -------------------------------
def draw_ui(frame):
    cv2.rectangle(frame, (0, 0), (640, 65), (50, 50, 50), -1)

    cv2.rectangle(frame, (10, 10), (110, 55), (0, 0, 0), -1)
    cv2.putText(frame, "CLEAR", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.rectangle(frame, (130, 10), (210, 55), (255, 0, 0), -1)
    cv2.rectangle(frame, (230, 10), (310, 55), (0, 255, 0), -1)
    cv2.rectangle(frame, (330, 10), (410, 55), (0, 0, 255), -1)
    cv2.rectangle(frame, (430, 10), (510, 55), (0, 255, 255), -1)

# -------------------------------
# 4. Capture Video
# -------------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    draw_ui(frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Index finger tip (Landmark 8)
            x = int(hand_landmarks.landmark[8].x * 640)
            y = int(hand_landmarks.landmark[8].y * 480)

            # Thumb tip (Landmark 4)
            thumb_y = int(hand_landmarks.landmark[4].y * 480)

            # Draw pointer
            cv2.circle(frame, (x, y), 8, colors[color_index], -1)

            # Gesture: If thumb close to index -> selection mode
            if abs(y - thumb_y) < 30:
                if y <= 65:
                    # Button interactions
                    if 10 <= x <= 110:
                        # Clear
                        blue_points = [deque(maxlen=1024)]
                        green_points = [deque(maxlen=1024)]
                        red_points = [deque(maxlen=1024)]
                        yellow_points = [deque(maxlen=1024)]

                        blue_index = green_index = red_index = yellow_index = 0
                        paint_window[:] = 255

                    elif 130 <= x <= 210:
                        color_index = 0
                    elif 230 <= x <= 310:
                        color_index = 1
                    elif 330 <= x <= 410:
                        color_index = 2
                    elif 430 <= x <= 510:
                        color_index = 3
            else:
                # Drawing mode
                if color_index == 0:
                    blue_points[blue_index].appendleft((x, y))
                elif color_index == 1:
                    green_points[green_index].appendleft((x, y))
                elif color_index == 2:
                    red_points[red_index].appendleft((x, y))
                elif color_index == 3:
                    yellow_points[yellow_index].appendleft((x, y))

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    else:
        # New stroke when hand disappears
        blue_points.append(deque(maxlen=1024))
        green_points.append(deque(maxlen=1024))
        red_points.append(deque(maxlen=1024))
        yellow_points.append(deque(maxlen=1024))

        blue_index += 1
        green_index += 1
        red_index += 1
        yellow_index += 1

    # -------------------------------
    # 5. Draw Lines
    # -------------------------------
    for i in range(len(blue_points)):
        for j in range(1, len(blue_points[i])):
            if blue_points[i][j - 1] is None or blue_points[i][j] is None:
                continue
            cv2.line(frame, blue_points[i][j - 1], blue_points[i][j], colors[0], 2)
            cv2.line(paint_window, blue_points[i][j - 1], blue_points[i][j], colors[0], 2)

    for i in range(len(green_points)):
        for j in range(1, len(green_points[i])):
            if green_points[i][j - 1] is None or green_points[i][j] is None:
                continue
            cv2.line(frame, green_points[i][j - 1], green_points[i][j], colors[1], 2)
            cv2.line(paint_window, green_points[i][j - 1], green_points[i][j], colors[1], 2)

    for i in range(len(red_points)):
        for j in range(1, len(red_points[i])):
            if red_points[i][j - 1] is None or red_points[i][j] is None:
                continue
            cv2.line(frame, red_points[i][j - 1], red_points[i][j], colors[2], 2)
            cv2.line(paint_window, red_points[i][j - 1], red_points[i][j], colors[2], 2)

    for i in range(len(yellow_points)):
        for j in range(1, len(yellow_points[i])):
            if yellow_points[i][j - 1] is None or yellow_points[i][j] is None:
                continue
            cv2.line(frame, yellow_points[i][j - 1], yellow_points[i][j], colors[3], 2)
            cv2.line(paint_window, yellow_points[i][j - 1], yellow_points[i][j], colors[3], 2)

    # -------------------------------
    # 6. Show Output
    # -------------------------------
    cv2.imshow("Air Canvas", frame)
    cv2.imshow("Canvas", paint_window)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# -------------------------------
# 7. Cleanup
# -------------------------------
cap.release()
cv2.destroyAllWindows()
