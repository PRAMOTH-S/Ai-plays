# 🎭 AI-Powered Presentation Air Clicke

<p align="center">
  Control your presentations using **hand gestures in mid-air**.  
  No hardware clicker. No touching the keyboard. Just gesture and present.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/PyAutoGUI-Automation-red?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/github/stars/PRAMOTH-S?style=for-the-badge">
</p>

---

# 📌 Overview

**AI-Powered Presentation Air Clicker** is a computer vision based tool that allows speakers to control presentation slides using **hand gestures detected via a webcam**.

It uses **MediaPipe hand landmark detection** to track finger positions and **PyAutoGUI** to send keyboard commands to presentation software like:

- Microsoft PowerPoint  
- Google Slides  
- Canva Presentations  

This removes the need for **physical clickers** and enables a **touchless presentation experience**.

---

# 🧠 How It Works

1. Webcam captures live video feed.
2. **MediaPipe** detects 21 hand landmarks.
3. Gesture recognition logic interprets finger positions.
4. Recognized gestures trigger **keyboard events** using PyAutoGUI.
5. The presentation software receives the commands.

```
Webcam → OpenCV → MediaPipe → Gesture Detection → PyAutoGUI → Presentation Control
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|--------|
| **Python 3.11** | Core programming language |
| **OpenCV** | Video capture & visual interface |
| **MediaPipe** | Real-time hand landmark detection |
| **PyAutoGUI** | Keyboard automation |

---

# ✨ Features

✔ Touchless slide navigation  
✔ Works with PowerPoint / Canva / Google Slides  
✔ Real-time gesture recognition  
✔ Floating HUD preview window  
✔ Intelligent debounce system to prevent rapid skipping  
✔ Simple lightweight Python implementation  

---

# 🎮 Gesture Controls

| Gesture | Action | Keyboard Mapping |
|-------|-------|-------|
| 🤏 **Pinch (Index + Thumb)** | Next Slide | `DOWN` Arrow |
| ✋ **Full Palm (High Five)** | Previous Slide | `UP` Arrow |
| ☝ **Index Finger Hover** | Laser Pointer Simulation | Visual Feedback |

---

# 🖥 System Architecture

```
                +------------------+
                |      Webcam      |
                +--------+---------+
                         |
                         v
                +------------------+
                |      OpenCV      |
                | Video Processing |
                +--------+---------+
                         |
                         v
                +------------------+
                |    MediaPipe     |
                | Hand Detection   |
                +--------+---------+
                         |
                         v
                +------------------+
                | Gesture Analyzer |
                +--------+---------+
                         |
                         v
                +------------------+
                |    PyAutoGUI     |
                | Keyboard Events  |
                +--------+---------+
                         |
                         v
                +------------------+
                | Presentation App |
                +------------------+
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/PRAMOTH-S/Air-Clicker.git
cd Air-Clicker
```

---

## 2️⃣ Install Dependencies

```bash
pip install numpy==1.26.4
pip install opencv-python==4.10.0.84
pip install mediapipe==0.10.14
pip install pyautogui
```

Or install everything together:

```bash
pip install numpy opencv-python mediapipe pyautogui
```

---

# ▶ Running the Application

1️⃣ Open your presentation (PowerPoint / Canva / Google Slides)

2️⃣ Run the Python script

```bash
python main.py
```

3️⃣ Click on the presentation window to give it **system focus**

4️⃣ Perform gestures in front of your webcam 🎥

---

# 📷 Demo

*(Add screenshots or GIFs here)*

Example:

```
/demo/demo.gif
```

or

```
![Demo](demo/demo.gif)
```

---

# ⚙️ Requirements

- Python **3.9 – 3.11**
- Webcam
- Windows / macOS / Linux

---

# 📂 Project Structure

```
Air-Clicker
│
├── main.py
├── requirements.txt
├── README.md
└── demo
    └── demo.gif
```

---

# 📈 Future Improvements

- Gesture based **mouse control**
- AI gesture training system
- Multi-hand gesture support
- Virtual laser pointer tracking
- Presentation timer overlay

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a feature branch  

```
git checkout -b feature-name
```

3. Commit your changes  

```
git commit -m "Add new feature"
```

4. Push to GitHub  

```
git push origin feature-name
```

5. Open a Pull Request

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
🔗 Share it with others

---

# 👨‍💻 Author

**Pramoth S**

GitHub:  
https://github.com/PRAMOTH-S

---

# 📜 License

This project is licensed under the **MIT License**.

```
MIT License
Copyright (c) 2026 Pramoth
```

---
