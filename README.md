# Hand Gesture PC Controller

A computer vision project that enables users to control their computer using hand gestures detected through a webcam. The system uses **MediaPipe** for hand tracking and **OpenCV** for real-time video processing. Different gestures trigger different system actions such as opening applications, minimizing windows, or locking the screen.

---

## Features

* Real-time hand detection using MediaPipe
* Finger counting based on hand landmark coordinates
* Gesture-based computer control
* Webcam-based real-time interaction
* Automation of system commands using PyAutoGUI

---

## How It Works

1. The webcam captures live video frames.
2. Frames are processed using OpenCV.
3. MediaPipe detects hand landmarks in the frame.
4. The program analyzes finger positions to determine how many fingers are raised.
5. Each finger count corresponds to a predefined system action.

---

## Gesture Controls

| Finger Count | Action             |
| ------------ | ------------------ |
| 1            | Show Desktop       |
| 2            | Open Google Chrome |
| 3            | Open Notepad       |
| 4            | Lock Screen        |
| 5            | Open Task Manager  |

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/hand-gesture-controller.git
cd hand-gesture-controller
```

Install the required dependencies:

```bash
pip install opencv-python mediapipe pyautogui
```

---

## Running the Project

Run the Python script:

```bash
python main.py
```

Press **Q** to exit the application.

---

## Future Improvements

* Add custom gesture recognition (thumbs up, peace sign, etc.)
* Implement gesture smoothing to avoid repeated triggers
* Add a graphical interface to display detected gestures
* Integrate volume and media control
* Support for multiple gesture commands

---

## Applications

* Touchless computer control
* Accessibility tools for hands-free interaction
* Gesture-based human-computer interaction systems
* Smart home automation

---

## Author

Your Name
GitHub: https://github.com/joy-programs
LinkedIn: https://linkedin.com/in/joy-kh
