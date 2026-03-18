import cv2
import mediapipe as mp
import pygame
import math
import numpy as np

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 80)

# Keyboard Layout (Added Backspace and Space)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "<-"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", " "]]

typed_text = ""

class Key():
    def __init__(self, x, y, char, w=80, h=80):
        self.x = x
        self.y = y
        self.char = char
        self.w = w
        self.h = h

    def draw(self, screen, is_hovered=False, is_pressed=False):
        # Color Logic: Cyan for hover, White for normal, Pink for click
        color = (200, 200, 200)
        thickness = 2
        if is_hovered: 
            color = (0, 255, 255)
            thickness = 4
        if is_pressed: 
            color = (255, 0, 255)
            thickness = 6
        
        # Draw soft rounded corners
        pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.h), thickness, border_radius=12)
        
        # Center the text
        label = "BS" if self.char == "<-" else "SPACE" if self.char == " " else self.char
        text_surface = font.render(label, True, color)
        text_rect = text_surface.get_rect(center=(self.x + self.w//2, self.y + self.h//2))
        screen.blit(text_surface, text_rect)

# Generate Key Objects
keyboard_objs = []
for i, row in enumerate(keys):
    for j, char in enumerate(row):
        w = 200 if char == " " else 100 if char == "<-" else 80
        keyboard_objs.append(Key(110 * j + 100, 110 * i + 250, char, w=w))

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

running = True
last_char = ""

while running:
    ret, frame = cap.read()
    if not ret: break
    
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Convert OpenCV frame to Pygame Surface (The Background)
    # This prevents the "Grey Screen" issue
    frame_surface = pygame.surfarray.make_surface(cv2.transpose(img_rgb))
    screen.blit(frame_surface, (0, 0))

    cursor_pos = None
    clicking = False

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            idx_x = int(hand_lms.landmark[8].x * WIDTH)
            idx_y = int(hand_lms.landmark[8].y * HEIGHT)
            cursor_pos = (idx_x, idx_y)

            thumb_x = int(hand_lms.landmark[4].x * WIDTH)
            thumb_y = int(hand_lms.landmark[4].y * HEIGHT)
            distance = math.hypot(idx_x - thumb_x, idx_y - thumb_y)
            
            if distance < 35: 
                clicking = True

            # Draw a futuristic "target" cursor
            pygame.draw.circle(screen, (0, 255, 255), (idx_x, idx_y), 20, 2)
            pygame.draw.circle(screen, (0, 255, 255), (idx_x, idx_y), 2)

    # Keyboard Logic
    for key in keyboard_objs:
        hover = False
        if cursor_pos:
            if key.x < cursor_pos[0] < key.x + key.w and key.y < cursor_pos[1] < key.y + key.h:
                hover = True
                if clicking and last_char != key.char:
                    if key.char == "<-":
                        typed_text = typed_text[:-1] # Backspace logic
                    else:
                        typed_text += key.char
                    last_char = key.char 
                
        if not clicking:
            last_char = ""

        key.draw(screen, is_hovered=hover, is_pressed=(hover and clicking))

    # Glassy Text Box Overlay
    pygame.draw.rect(screen, (0, 0, 0), (100, 50, 1080, 100), border_radius=15)
    pygame.draw.rect(screen, (0, 255, 255), (100, 50, 1080, 100), 2, border_radius=15)
    result_surface = big_font.render(typed_text, True, (255, 255, 255))
    screen.blit(result_surface, (130, 70))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

cap.release()
pygame.quit()
