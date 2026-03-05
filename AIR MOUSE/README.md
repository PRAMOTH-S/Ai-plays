# 🖱️ Air Mouse Pro – AI Gesture-Based Virtua Mouse

Air Mouse Pro is a computer vision project that enables users to control their system mouse using **hand gestures detected through a webcam**.  
The application uses **MediaPipe Hand Tracking** to detect hand landmarks and converts finger movements into real-time mouse actions such as cursor movement, clicking, and scrolling.

This project demonstrates the use of **Artificial Intelligence, Computer Vision, and Human-Computer Interaction (HCI)** to build a touchless control interface.

---

<p align="center">

<img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv&logoColor=white" />
<img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
<img src="https://img.shields.io/github/stars/PRAMOTH-S/Ai-plays?style=for-the-badge" />

</p>

## 🚀 Features

- **Real-Time Cursor Control**
  - Move the cursor using the **index finger tip**.

- **Left Click Gesture**
  - Perform a **pinch gesture between the Index Finger and Thumb**.

- **Right Click Gesture**
  - Perform a **pinch gesture between the Middle Finger and Thumb**.

- **Scroll Gesture**
  - Extend the **Ring Finger** and move your hand vertically to scroll.

- **Cursor Smoothing**
  - Reduces cursor jitter using interpolation for smoother movement.

- **Visual Hand Tracking**
  - Displays detected hand landmarks and skeleton connections on the camera feed.

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV** – Camera input and frame processing
- **MediaPipe** – Hand landmark detection
- **PyAutoGUI** – Mouse automation
- **NumPy** – Coordinate interpolation and calculations

---

## 📂 Project Structure

```
Air-Mouse-Pro/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PRAMOTH-S/Ai-plays.git
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui numpy
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 🎮 Gesture Controls

| Gesture | Action |
|------|------|
| Move Index Finger | Move Cursor |
| Index + Thumb Pinch | Left Click |
| Middle + Thumb Pinch | Right Click |
| Ring Finger Extended + Vertical Movement | Scroll |

---

## 🧠 How It Works

1. The webcam captures real-time video frames.
2. MediaPipe detects **21 hand landmarks**.
3. The **index finger tip position** is mapped to screen coordinates.
4. Distance between fingers is calculated to detect gestures.
5. Detected gestures trigger mouse actions using **PyAutoGUI**.

---

## 📐 Gesture Detection Logic

The system calculates the **Euclidean Distance** between finger landmarks.

For example, the distance between the **Thumb (Landmark 4)** and **Index Finger (Landmark 8)** is calculated as:

\[
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
\]

If the distance falls below a threshold value, the system triggers a **mouse click event**.

---

## 🎥 Application Workflow

1. Capture webcam frame
2. Detect hand landmarks using MediaPipe
3. Map finger position to screen coordinates
4. Detect gestures
5. Trigger mouse events
6. Display visual feedback

---

## 🚀 Future Improvements

- Multi-hand gesture support
- Drag and drop gesture
- Gesture sensitivity settings
- Graphical interface for configuration
- Performance optimization for low-end systems

---

## 👨‍💻 Author

Developed as a **Computer Vision and Artificial Intelligence project** exploring gesture-based interaction systems.

---

⭐ If you found this project useful, consider giving the repository a **star**.
