# ⌨️ Air-Typing Keyboard (AI-Powered Virtual UI)

A futuristic, gesture-controlled virtual keyboard built with **Computer Vision**. This project allows users to type in mid-air by tracking hand movements and finger "clicks" (pinch gestures) using a webcam. 

Designed for high engagement on platforms like **TikTok and Instagram**, featuring a "holographic" HUD and real-time interactive feedback.



## ✨ Features
* **Real-time Hand Tracking:** Uses MediaPipe to track 21 hand landmarks at high FPS.
* **Gesture Recognition:** Intelligent "Pinch-to-Click" detection by calculating Euclidean distance between the index finger and thumb.
* **Holographic UI:** A semi-transparent Pygame overlay that creates an Augmented Reality (AR) effect.
* **Full Keyboard Logic:** Includes A-Z, Spacebar, and a functional Backspace system.
* **Visual Feedback:** Dynamic color shifting (Cyan for hover, Magenta for click) to provide UX feedback.

## 🚀 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) | **Python 3.11** - Core Logic |
| ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) | **OpenCV 4.10.0** - Image Processing |
| ![MediaPipe](https://img.shields.io/badge/MediaPipe-007f7b?style=for-the-badge&logo=google&logoColor=white) | **MediaPipe 0.10.1** - Hand Landmark Tracking |
| ![Pygame](https://img.shields.io/badge/Pygame-33cc33?style=for-the-badge&logo=python&logoColor=white) | **Pygame** - Virtual UI and Rendering |
| ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) | **NumPy 1.26.4** - Matrix Calculations |

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jemelimercy/air-typing-keyboard.git](https://github.com/jemelimercy/Air-Typing-Keyboard.git)
   cd Air-Typing-Keyboard

2. Set up a Virtual Environment (Recommended):
    py -3.11 -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

3. Install Dependencies:
pip install opencv-python==4.10.0.84 mediapipe==0.10.14 numpy==1.26.4 pygame

🎮 How to Use
Run the script: python main.py

Position your hand so the webcam can see your palm.

Move: Use your Index Finger Tip as the mouse cursor to hover over keys.

Type: Bring your Thumb and Index Finger together (pinch) to "click" a key.

Delete: Use the BS (Backspace) key at the top right to fix typos.

🛠 Project Structure
main.py: The core application containing the Pygame loop and MediaPipe logic.

.gitignore: Prevents environment files and cache from being uploaded.

assets/: (Optional) Folder for click sounds or custom fonts.