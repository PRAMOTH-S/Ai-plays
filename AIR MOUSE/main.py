import os
import warnings

# 1. Suppress MediaPipe/Protobuf deprecation warnings and logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore", category=UserWarning, module='google.protobuf.symbol_database')

import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# 2. Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands_detector = mp_hands.Hands(
    max_num_hands=1, 
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

# 3. Screen Setup
screen_w, screen_h = pyautogui.size()
pyautogui.FAILSAFE = True # Move mouse to top-left corner to stop script

# 4. Camera Setup
cap = cv2.VideoCapture(0)

# Smoothing variables (reduces jitter)
prev_x, prev_y = 0, 0
smooth_factor = 5 

while True:
    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1)
    f_h, f_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hands_detector.process(rgb_frame)
    results = output.multi_hand_landmarks

    if results:
        for hand_landmarks in results:
            # --- DRAW VISUALS (Red Lines, White Dots) ---
            mp_draw.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=3),
                mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2)
            )

            landmarks = hand_landmarks.landmark
            
            # 5. TRACKING (Index Finger Tip - ID 8)
            index_tip = landmarks[8]
            ix, iy = int(index_tip.x * f_w), int(index_tip.y * f_h)
            
            # Map camera coordinates to screen resolution
            mouse_x = np.interp(ix, (0, f_w), (0, screen_w))
            mouse_y = np.interp(iy, (0, f_h), (0, screen_h))
            
            # Apply Smoothing Logic
            curr_x = prev_x + (mouse_x - prev_x) / smooth_factor
            curr_y = prev_y + (mouse_y - prev_y) / smooth_factor
            
            # 6. SCROLL LOGIC (Ring Finger - ID 16)
            # If Ring finger is extended (higher than its knuckle ID 14)
            if landmarks[16].y < landmarks[14].y:
                scroll_amount = int((prev_y - curr_y) * 4) # Adjust multiplier for speed
                pyautogui.scroll(scroll_amount)
                cv2.putText(frame, "SCROLLING", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            else:
                pyautogui.moveTo(curr_x, curr_y)
            
            prev_x, prev_y = curr_x, curr_y

            # 7. CLICK LOGIC (Pinch Distance)
            thumb = landmarks[4]
            tx, ty = int(thumb.x * f_w), int(thumb.y * f_h)
            
            # Left Click: Index to Thumb
            dist_left = ((ix - tx)**2 + (iy - ty)**2)**0.5
            
            # Right Click: Middle to Thumb (ID 12)
            middle_tip = landmarks[12]
            mx, my = int(middle_tip.x * f_w), int(middle_tip.y * f_h)
            dist_right = ((mx - tx)**2 + (my - ty)**2)**0.5

            if dist_left < 35:
                pyautogui.click()
                cv2.putText(frame, "LEFT CLICK", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                pyautogui.sleep(0.1)
                
            elif dist_right < 35:
                cv2.putText(frame, "RIGHT CLICK", (f_w - 250, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                pyautogui.rightClick()
                pyautogui.sleep(0.1)

    cv2.imshow('Air Mouse Pro', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()