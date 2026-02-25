import cv2
import numpy as np
import mediapipe as mp
import os

# 1. Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# 2. Safety-First Overlay Function
def overlay_png(bg, img_obj, x, y):
    if img_obj is None: return bg
    
    # Get dimensions
    h, w = img_obj.shape[:2]
    bg_h, bg_w = bg.shape[:2]

    # PREVENT CRASH: If image is even partially off-screen, we skip drawing it
    # This is likely why your game was closing during jumps
    if x < 0 or y < 0 or x + w > bg_w or y + h > bg_h:
        return bg

    try:
        img_rgb = img_obj[:, :, :3]
        alpha = img_obj[:, :, 3] / 255.0
        for c in range(3):
            bg[y:y+h, x:x+w, c] = (1.0 - alpha) * bg[y:y+h, x:x+w, c] + alpha * img_rgb[:, :, c]
    except Exception:
        pass # If any math error occurs, just keep the game running
    return bg

# 3. Load Assets
dino_img = cv2.imread('dino.png', cv2.IMREAD_UNCHANGED)
cactus_img = cv2.imread('cactus.png', cv2.IMREAD_UNCHANGED)

# Resize assets to safe sizes
if dino_img is not None: dino_img = cv2.resize(dino_img, (60, 60))
if cactus_img is not None: cactus_img = cv2.resize(cactus_img, (40, 60))

class Dino:
    def __init__(self):
        self.reset()
    def reset(self):
        self.x, self.y = 50, 300
        self.vel, self.grav = 0, 1.8
        self.is_jump = False
    def jump(self):
        if not self.is_jump:
            self.vel = -25
            self.is_jump = True
    def update(self):
        if self.is_jump:
            self.y += self.vel
            self.vel += self.grav
            # Safety: Don't let dino fly off the top
            if self.y < 10: 
                self.y = 10
                self.vel = 0
            # Land on ground
            if self.y >= 300:
                self.y = 300
                self.is_jump = False

class Obstacle:
    def __init__(self):
        self.reset()
    def reset(self):
        self.x, self.y = 640, 300
        self.speed = 14
    def update(self):
        self.x -= self.speed
        if self.x < -50:
            self.x = 640
            return True # Point scored
        return False

# 4. Initialization
player = Dino()
cactus = Obstacle()
score = 0
game_state = "PLAYING"
cap = cv2.VideoCapture(0)

print("Game Started! Close the window or press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    if game_state == "PLAYING":
        # Hand tracking
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0].landmark
            # Distance between Thumb(4) and Index(8)
            dist = np.sqrt((lm[4].x - lm[8].x)**2 + (lm[4].y - lm[8].y)**2)
            if dist > 0.15: # Gesture to jump
                player.jump()

        player.update()
        if cactus.update():
            score += 1
            cactus.speed += 0.2

        # TIGHT COLLISION DETECTION
        # Only trigger game over if dino is low AND touching the cactus horizontally
        if (cactus.x < player.x + 45 and cactus.x + 20 > player.x):
            if player.y > 280: # Dino must be close to ground to hit
                game_state = "GAMEOVER"

    # 5. Drawing
    # Draw a Ground Line
    cv2.line(frame, (0, 360), (640, 360), (255, 255, 255), 2)
    
    # Draw Sprites
    frame = overlay_png(frame, dino_img, int(player.x), int(player.y))
    frame = overlay_png(frame, cactus_img, int(cactus.x), int(cactus.y))

    # UI
    cv2.putText(frame, f"SCORE: {score}", (480, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)

    if game_state == "GAMEOVER":
        cv2.rectangle(frame, (100, 180), (540, 280), (0, 0, 0), -1)
        cv2.putText(frame, "CRASHED! Press 'R' to Restart", (120, 240), 
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Webcam Dino", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): break
    if key == ord('r'):
        player.reset()
        cactus.reset()
        score = 0
        game_state = "PLAYING"

cap.release()
cv2.destroyAllWindows()