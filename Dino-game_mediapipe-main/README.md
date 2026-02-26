# 🦖 Gesture-Controlled Dino Run  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8--3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/MediaPipe-HandTracking-green?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/OpenCV-ComputerVision-red?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/Pygame-GameEngine-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/AI-GestureControl-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge">
</p>

---

## 📌 Overview  

An AI-powered recreation of the classic **Chrome Dino Game**, controlled entirely through real-time hand gestures instead of a keyboard.  

This project demonstrates how **computer vision** can be used to build touchless, interactive applications using a webcam.

---

## 🎯 Features  

- ✋ Gesture-based jump control  
- ⚡ Real-time hand tracking with low latency  
- 🎮 Classic endless runner gameplay  
- 📷 Webcam-based interaction  
- 🧠 AI-powered hand landmark detection  

---

## 🕹️ How It Works  

The system captures live video using **OpenCV** and processes each frame using **MediaPipe**.

### Core Logic  

- Detect hand landmarks  
- Track:
  - Landmark **0 → Wrist**
  - Landmark **9 → Middle Finger MCP**
- Compute Euclidean distance  
- Trigger jump when threshold is exceeded  

---

## 📐 Mathematical Model  

The system uses the Euclidean distance formula:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

### Jump Condition  

```python
if current_dist > (initial_dist * 1.2):
    perform_jump()
