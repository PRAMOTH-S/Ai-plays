import cv2
import numpy as np
import mediapipe as mp
import pip 
import random

# 1. Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# 2. Particle Class
class Particle:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.w)
        self.y = random.randint(-self.h, 0) # Start above screen
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(2, 5)
        self.color = (random.randint(100, 255), random.randint(150, 255), 255)

    def update(self, finger_pos=None):
        # Apply Gravity
        self.vy += 0.1
        
        # Interaction with Finger (Repulsion)
        if finger_pos:
            fx, fy = finger_pos
            dx = self.x - fx
            dy = self.y - fy
            dist = np.sqrt(dx**2 + dy**2)
            
            if dist < 80: # Interaction radius
                # Calculate push force
                force = (80 - dist) * 0.2
                self.vx += (dx / dist) * force
                self.vy += (dy / dist) * force

        # Move particle
        self.x += self.vx
        self.y += self.vy

        # Air friction
        self.vx *= 0.99
        self.vy *= 0.99

        # Reset if out of bounds
        if self.y > self.h or self.x < 0 or self.x > self.w:
            self.reset()

# 3. Initialize Particles
WIDTH, HEIGHT = 640, 480
num_particles = 150
particles = [Particle(WIDTH, HEIGHT) for _ in range(num_particles)]

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (WIDTH, HEIGHT))
    
    # Process Hand
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    finger_pos = None
    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark[8]
        finger_pos = (int(lm.x * WIDTH), int(lm.y * HEIGHT))
        # Draw the "Force Field" around your finger
        cv2.circle(img, finger_pos, 80, (255, 255, 255), 1)

    # Update and Draw Particles
    for p in particles:
        p.update(finger_pos)
        cv2.circle(img, (int(p.x), int(p.y)), 3, p.color, -1)

    cv2.imshow("Fluid Particle Simulation", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
