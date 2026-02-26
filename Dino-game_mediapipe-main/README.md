# 🦖 Gesture-Controlled Dino Run

An AI-powered recreation of the classic "Chrome Dino" game. Instead of using a keyboard, players control the Dino's jumps through real-time hand gesture recognition using **Python** and **MediaPipe**.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MediaPipe](https://img.shields.io/badge/MediaPipe-007f00?style=for-the-badge&logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

---

## 🕹️ How it Works
The system uses the computer's webcam to track specific hand landmarks. By calculating the vertical distance between the **Wrist** and the **Middle Finger MCP**, the script triggers a "Jump" command whenever a specific threshold is crossed.

### Key Logic:
- **Gesture Trigger**: A jump is registered when the distance between Landmark 0 (Wrist) and Landmark 9 (Middle Finger MCP) exceeds a dynamic threshold.
- **Latency Management**: Optimized frame processing to ensure the Dino jumps the moment you move your hand.

---

## 📝 Mathematical Concept

The game relies on the Euclidean distance formula to determine hand state. If the distance $d$ between the wrist $(x_1, y_1)$ and the finger $(x_2, y_2)$ is greater than the threshold $T$, the jump function is called.

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

The jump condition is defined as:
```python
if current_dist > (initial_dist * 1.2):
    perform_jump()
    
    🚀 Installation & Setup
Clone the repository:
git clone [https://github.com/Jemelimercy/Dino-game_mediapipe.git](https://github.com/Jemelimercy/Dino-game_mediapipe.git)

Install dependencies:
pip install -r requirements.txt

Launch the game:
python dino_game.py

🛠️ Tech Stack
MediaPipe: For high-fidelity hand landmark detection.

OpenCV: For camera feed processing and image flipping.

Pygame: To handle the game loop, physics, and rendering.

Developed by Jemeli Mercy