import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# 1. Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, 
    max_num_hands=1, 
    min_detection_confidence=0.8, 
    min_tracking_confidence=0.8
)
mp_draw = mp.solutions.drawing_utils

# 2. Control Variables
delay_counter = 0
GESTURE_COOLDOWN = 25  # Prevents skipping multiple slides at once
status_text = "Ready"
status_color = (0, 255, 0)

# 3. Initialize Camera
cap = cv2.VideoCapture(0)

print("--- Presentation Air Clicker Active ---")
print("Pinch (Index + Thumb) = NEXT SLIDE")
print("Full Palm Up = PREVIOUS SLIDE ")
print("Press 'q' to exit")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip frame for mirror effect and get dimensions
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    # Convert to RGB for MediaPipe
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            lms = hand_lms.landmark
            
            # Get coordinates for Index (8) and Thumb (4)
            index_tip = (int(lms[8].x * w), int(lms[8].y * h))
            thumb_tip = (int(lms[4].x * w), int(lms[4].y * h))
            
            # Calculate pinch distance
            distance = np.hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])

            # Check which fingers are up (for the Palm gesture)
            fingers = []
            # Index, Middle, Ring, Pinky
            for tip in [8, 12, 16, 20]:
                if lms[tip].y < lms[tip - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # --- GESTURE LOGIC ---
            
            # 1. NEXT SLIDE: Pinch (Distance < 35)
            if distance < 35 and delay_counter == 0:
                pyautogui.press('down')
                status_text = "NEXT SLIDE "
                status_color = (0, 255, 0) # Green
                delay_counter = 1

            # 2. PREVIOUS SLIDE: All 4 fingers extended + Thumb away
            elif all(f == 1 for f in fingers) and delay_counter == 0:
                pyautogui.press('up')
                status_text = "PREVIOUS SLIDE"
                status_color = (255, 0, 0) # Blue
                delay_counter = 1

            # --- VISUAL FEEDBACK (HUD) ---
            # Draw a circle on the index finger (the "laser pointer")
            pointer_color = (0, 255, 0) if distance < 35 else (255, 0, 255)
            cv2.circle(frame, index_tip, 12, pointer_color, cv2.FILLED)
            
            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

    # Cooldown timer to prevent accidental double-clicks
    if delay_counter > 0:
        delay_counter += 1
        if delay_counter > GESTURE_COOLDOWN:
            delay_counter = 0
            status_text = "Ready"
            status_color = (0, 255, 0)

    # Add HUD Text
    cv2.rectangle(frame, (0, 0), (w, 60), (30, 30, 30), cv2.FILLED)
    cv2.putText(frame, f"STATUS: {status_text}", (20, 40), 
                cv2.FONT_HERSHEY_DUPLEX, 1, status_color, 2)

    # Show the Window
    window_name = "Presentation Controller"
    cv2.imshow(window_name, frame)
    
    # Keep window on top (Best for recording!)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()