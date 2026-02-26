# 🦖 Gesture-Controlled Dino Run  

An AI-powered recreation of the classic Chrome Dino game, controlled entirely through real-time hand gestures using computer vision.

---

## 📌 Overview  

This project replaces traditional keyboard input with gesture-based interaction. Using a webcam, the system detects hand movements and converts them into in-game actions like jumping.

---

## 🎯 Features  

- ✋ Gesture-based controls (no keyboard required)  
- ⚡ Real-time hand tracking with low latency  
- 🎮 Classic Dino endless runner gameplay  
- 📷 Webcam-based interaction  
- 🧠 MediaPipe-powered landmark detection  

---

## 🕹️ How It Works  

- Captures webcam video using OpenCV  
- Detects hand landmarks using MediaPipe  
- Tracks:
  - Landmark 0 → Wrist  
  - Landmark 9 → Middle Finger MCP  
- Calculates distance between these points  
- Triggers jump when distance exceeds threshold  

---

## 📐 Mathematical Model  

Euclidean distance formula:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

### Jump Condition:
```python
if current_dist > (initial_dist * 1.2):
    perform_jump()
