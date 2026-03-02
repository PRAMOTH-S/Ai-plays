# 🍎 AI Fruit-Ninja: Augmented Reality Edition

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-007f00?style=for-the-badge&logo=google&logoColor=white)
![Pygame](https://img.shields.io/badge/pygame-373737?style=for-the-badge&logo=python&logoColor=green)

---

## 📌 Overview
AI Fruit-Ninja is a real-time **Augmented Reality (AR) game** that allows users to slice virtual fruits using hand gestures.  
It uses **MediaPipe hand tracking** to convert the user's index finger into a virtual blade and overlays interactive game elements onto a live webcam feed.

---

## 🚀 Key Features

- 🎯 **Real-Time Hand Tracking** using MediaPipe
- 🕹️ **AR Gameplay** with live webcam integration
- ✨ **Smooth Collision Detection** using geometric algorithms
- 🔴 **Custom Hand Landmark Visualization**
- 💥 **Particle Effects** for fruit slicing feedback
- ♾️ **Infinite Gameplay Loop** with scoring system

---

## 🧠 How It Works

1. Webcam captures live video
2. MediaPipe detects hand landmarks
3. Index finger tip is tracked across frames
4. A swipe is formed using:
   - Previous position → **A**
   - Current position → **B**
5. Collision is detected using math (explained below)

---

## 📐 Collision Detection Algorithm

Traditional collision detection fails during fast movements because objects may skip frames.

To solve this, we compute the **distance between a fruit's center point (P)** and the **line segment formed by finger movement (A → B)**.

### Formula:

\[
d = \frac{|(y_B - y_A)x_P - (x_B - x_A)y_P + x_B y_A - y_B x_A|}{\sqrt{(y_B - y_A)^2 + (x_B - x_A)^2}}
\]

### Logic:

- If:
  \[
  d < \text{fruit radius}
  \]
  → ✅ Fruit is sliced

### Why This Works:

- Detects slicing even during **fast swipes**
- Prevents missed collisions between frames
- Provides **robust and smooth gameplay experience**

> ⚠️ Note: This operates in a 2D coordinate space derived from webcam input.

---

## 🛠️ Tech Stack

| Technology  | Role |
|------------|------|
| Python     | Core programming language |
| OpenCV     | Video capture & rendering |
| MediaPipe  | Hand tracking |
| Pygame     | Game mechanics & UI |

---
