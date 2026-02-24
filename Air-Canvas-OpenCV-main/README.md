# 🎨 Air Canvas: Gesture-Based Digital Sketchpad

A Computer Vision application that allows users to draw in mid-air using their index finger. By leveraging **MediaPipe** for hand tracking and **OpenCV** for canvas rendering, this project turns your webcam into a touchless drawing interface.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MediaPipe](https://img.shields.io/badge/MediaPipe-007f00?style=for-the-badge&logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

---

## 🚀 Key Features
- **Real-time Hand Tracking**: High-precision tracking of the index finger landmark.
- **Multi-Color Palette**: Interactive on-screen buttons to switch between Blue, Green, Red, and Yellow.
- **Canvas Clear**: Dedicated "Clear All" gesture/button to reset the drawing.
- **Brush Thickness Control**: Smooth rendering of lines using a series of connected points stored in deques.

---

## 🧪 Technical Logic

The application maintains several `collections.deque` objects to store the points for different colors. This ensures that the drawing remains smooth and doesn't cause memory leaks during long sessions.

### Mathematical Point Mapping:
The index finger landmark (ID 8) is mapped from normalized coordinates $(x, y)$ to the frame's pixel dimensions:

$$Px = x \times Width$$

$$Py = y \times Height$$

Whenever the finger is detected in the "Drawing Zone" (below the selection buttons), the points are appended to the active deque and connected using the `cv2.line` function.

---

## 🛠️ Installation

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/Jemelimercy/Air-Canvas.git](https://github.com/Jemelimercy/Air-Canvas.git)

   Install Dependencies:
   pip install opencv-python mediapipe numpy

   Run the App:
   python air_canvas.py

   Developed by Jemeli Mercy
