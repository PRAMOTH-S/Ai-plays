import cv2
import mediapipe as mp
import pygame
import random
import math
from collections import deque

# --- INITIALIZATION ---
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand-Ninja: Red Scan Mode")

# --- ASSET LOADING ---
try:
    swish_sound = pygame.mixer.Sound("swish.mp3")
    APPLE_IMG = pygame.transform.scale(pygame.image.load("apple.png"), (70, 70))
    BANANA_IMG = pygame.transform.scale(pygame.image.load("banana.png"), (80, 80))
    WATERMELON_IMG = pygame.transform.scale(pygame.image.load("watermelon.png"), (90,90))
    PINEAPPLE_IMG = pygame.transform.scale(pygame.image.load("pineapple.png"), (90,90))
    FRUIT_IMAGES = [APPLE_IMG, BANANA_IMG,WATERMELON_IMG,PINEAPPLE_IMG]
except:
    print("❌ Asset Error: Ensure apple.png, banana.png, watermelon.png and swish.mp3 are present.")
    pygame.quit(); exit()

# --- MEDIAPIPE SETUP ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
cap = cv2.VideoCapture(0)

# --- CLASSES (Fruit, Particle, Math) ---
# [Classes remain the same as previous Endless Precision version]
class Fruit:
    def __init__(self):
        self.image = random.choice(FRUIT_IMAGES)
        self.x, self.y = random.randint(100, WIDTH-100), HEIGHT
        self.vx, self.vy = random.uniform(-2, 2), random.uniform(-19, -15)
        self.gravity = 0.35
        self.radius = 35
    def update(self):
        self.x += self.vx; self.y += self.vy; self.vy += self.gravity
    def draw(self, surface):
        surface.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))

class Particle:
    def __init__(self, x, y, color):
        self.x, self.y, self.color = x, y, color
        self.vx, self.vy = random.uniform(-5, 5), random.uniform(-5, 5)
        self.life = 255
    def update(self):
        self.x += self.vx; self.y += self.vy; self.life -= 15

def dist_to_segment(p, a, b):
    px, py = p; ax, ay = a; bx, by = b
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0: return math.hypot(px - ax, py - ay)
    t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))

# --- GAME STATE ---
score = 0
fruits = []
particles = []
trail = deque(maxlen=8)
font = pygame.font.SysFont("Arial", 32, bold=True)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release(); pygame.quit(); exit()

    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    # --- 1. DRAW RED SKELETON MARKS ---
    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                rgb_frame, 
                hand_lms, 
                mp_hands.HAND_CONNECTIONS,
                # Landmark dots (Red)
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=3),
                # Connection lines (Red)
                mp_drawing.DrawingSpec(color=(200, 0, 0), thickness=2) 
            )

    bg_surface = pygame.surfarray.make_surface(rgb_frame.swapaxes(0, 1))
    screen.blit(bg_surface, (0, 0))

    curr_pos = None
    if result.multi_hand_landmarks:
        lm = result.multi_hand_landmarks[0].landmark[8]
        curr_pos = (int(lm.x * WIDTH), int(lm.y * HEIGHT))
        trail.append(curr_pos)

    # --- 2. GAME LOGIC ---
    if random.random() < 0.05: fruits.append(Fruit())
    for f in fruits[:]:
        f.update(); f.draw(screen)
        if len(trail) > 1 and curr_pos:
            if dist_to_segment((f.x, f.y), trail[-2], curr_pos) < f.radius:
                if swish_sound: swish_sound.play()
                p_col = (255, 0, 0) if f.image == APPLE_IMG else (255, 255, 0)
                for _ in range(12): particles.append(Particle(f.x, f.y, p_col))
                score += 1; fruits.remove(f); continue
        if f.y > HEIGHT + 50: fruits.remove(f)

    # Drawing Slicing Trail
    if len(trail) > 1:
        for i in range(len(trail)-1):
            pygame.draw.line(screen, (255, 0, 0), trail[i], trail[i+1], i + 3)

    # Particles
    for p in particles[:]:
        p.update()
        if p.life > 0:
            s = pygame.Surface((6, 6)); s.set_alpha(p.life); s.fill(p.color)
            screen.blit(s, (p.x, p.y))
        else: particles.remove(p)

    # --- 3. DRAW BLACK SCORE TAB ---
    # Create a small surface for the tab (semi-transparent)
    score_bg = pygame.Surface((160, 50))
    score_bg.set_alpha(180) # 0 is transparent, 255 is solid
    score_bg.fill((0, 0, 0)) # Black
    screen.blit(score_bg, (10, 10))
    
    score_text = font.render(f"SCORE: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 15))

    pygame.display.flip()
    clock.tick(60)
