# Hand Gesture Control Project README

## Introduction
Welcome to the Hand Gesture Control Project! This project is designed to let you control your computer's cursor using simple hand gestures. It's a fun and interactive way to interact with your machine using the power of computer vision and hand tracking.

## Features
- **Hand Gesture Recognition:** The software recognizes your hand gestures through a webcam.
- **Cursor Movement:** Move your computer's cursor by moving your hand.(Index finger Tip i.e index 8)
- **Clicking Action:** Perform a click action by a specific hand gesture.(Bringing close the thumb and the middle finger center, i.e. index 4 and index 10)
- Refer to the image to help your self!

## Prerequisites
To get started, you will need:
- Python 3.11.x installed on your computer.(or any other version that can run all the dependencies)
- A webcam or a camera module.

## Dependencies
Make sure to install these Python libraries:
- `opencv-python` for image processing.
- `mediapipe` for hand tracking.
- `pyautogui` for controlling the mouse cursor.

You can install them using pip:
```bash
pip install opencv-python mediapipe pyautogui
```

## Installation
1. Clone the repository:
   ```bash
   git clone [repository link]
   ```
2. Navigate to the cloned directory.

## Usage
1. Run the script:
   ```bash
   python hand_gesture_control.py
   ```
2. Show your hand to the webcam. The program will track your hand movements.
3. Move your hand to control the cursor.
4. Perform the specified gesture to click.

## How It Works
- The script uses `opencv` and `mediapipe` to detect and track hand landmarks.
- It then calculates the position of your index finger and moves the cursor accordingly.
- A specific gesture i.e. bringing your thumb and middle finger close is used to simulate a mouse left click.

## Customization
- You can adjust the `scale_factor` to change the sensitivity of cursor movement.
- Modify the distance(distance_int) threshold in the script for the click action.

## Image
 ![image](https://github.com/YashRaj9211/Python_MouseControlClick/assets/92658760/b583570f-e40c-4c99-aa59-fd424b694cfc)


## Contribution
Feel free to fork this project, make changes, and submit pull requests. Your contributions are welcome!

## Support
If you encounter any issues, please open an issue in the repository.

---

Start controlling your computer in a whole new way with this Hand Gesture Control Project! 🖐💻

---
