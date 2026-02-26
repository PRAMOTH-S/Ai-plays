# 🦖 Gesture-Controlled Dino Run  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/MediaPipe-Google-green?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/OpenCV-ComputerVision-red?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/Pygame-GameEngine-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge">
</p>

---

## 📌 Overview  

An AI-powered version of the classic **Chrome Dino Game**, controlled using real-time hand gestures instead of a keyboard.  

This project leverages **computer vision** to create a touchless gaming experience using a webcam, demonstrating practical applications of **Human-Computer Interaction (HCI)**.

---

## 🎯 Features  

- ✋ Gesture-based jump control  
- ⚡ Real-time hand tracking (low latency)  
- 🎮 Classic endless runner gameplay  
- 📷 Webcam-based interaction (no external hardware)  
- 🧠 AI-powered hand landmark detection  

---

## 🕹️ How It Works  

The system captures live video using OpenCV and processes each frame with MediaPipe.

### Core Logic:
- Detect hand landmarks using MediaPipe  
- Track:
  - Landmark **0 → Wrist**
  - Landmark **9 → Middle Finger MCP**
- Compute distance between these points  
- Trigger jump when threshold is exceeded  

---

## 📐 Mathematical Model  

The system uses Euclidean distance:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

### Jump Condition:
```python
if current_dist > (initial_dist * 1.2):
    perform_jump()
