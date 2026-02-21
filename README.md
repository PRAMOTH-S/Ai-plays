# ⌨️ Air-Typing Keyboard (AI-Powered Virtual UI)

A futuristic, gesture-controlled virtual keyboard built using **Computer Vision**.  
This project allows users to type in mid-air by tracking hand movements and detecting finger "clicks" (pinch gestures) using a webcam.

Designed for high engagement on platforms like **TikTok and Instagram**, featuring a holographic-style UI and real-time interactive feedback.

---

## ✨ Features

- **Real-time Hand Tracking:** Tracks 21 hand landmarks using MediaPipe with high FPS  
- **Gesture Recognition:** Detects "Pinch-to-Click" using Euclidean distance between thumb and index finger  
- **Holographic UI:** Semi-transparent Pygame overlay for AR-like experience  
- **Full Keyboard Support:** Includes A–Z, Spacebar, and Backspace  
- **Visual Feedback:**  
  - Cyan → Hover  
  - Magenta → Click  

---

## 🚀 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| Python 3.11 | Core Logic |
| OpenCV 4.10.0 | Image Processing |
| MediaPipe 0.10.14 | Hand Tracking |
| Pygame | UI Rendering |
| NumPy 1.26.4 | Calculations |

---
