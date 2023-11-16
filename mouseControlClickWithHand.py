import cv2
import mediapipe as mp
import math
import pyautogui

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe drawing utilities
mp_drawing = mp.solutions.drawing_utils

# Capture video from your webcam or another source
cap = cv2.VideoCapture(0)

# Constants for screen width and height
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# Initialize variables to store the previous hand position
prev_x, prev_y = 0, 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame horizontally to remove lateral inversion
    frame = cv2.flip(frame, 1)  # 1 means horizontal flip

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect landmarks on the hand
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for i, landmark in enumerate(landmarks.landmark):
                h, w, c = frame.shape
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                cv2.putText(frame, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

            scale_factor = 1.3
            # Calculate the position of index 8 (index finger tip)
            index8 = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert the position to screen coordinates with scaling
            cursor_x = int(index8.x * SCREEN_WIDTH * scale_factor)
            cursor_y = int(index8.y * SCREEN_HEIGHT * scale_factor)

            # Clamp the cursor coordinates to the screen boundaries
            cursor_x = max(0, min(cursor_x, SCREEN_WIDTH - 1))
            cursor_y = max(0, min(cursor_y, SCREEN_HEIGHT - 1))

            # Calculate distance using the Euclidean distance formula
            index4 = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index10 = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
            distance = math.sqrt((index4.x - index10.x) ** 2 + (index4.y - index10.y) ** 2)

            # Convert the distance to an integer for displaying on the line
            distance_int = int(distance * w)  # Convert normalized distance to pixels

            if(distance_int<35):
                pyautogui.click()
            # Draw a line between index 8 and index 4
            cv2.line(frame, (int(index10.x * w), int(index10.y * h)), (int(index4.x * w), int(index4.y * h)), (255, 0, 0), 2)

            # Display the distance on the line
            cv2.putText(frame, f"{distance_int} pixels", (int((index10.x + index4.x) * w / 2), int((index10.y + index4.y) * h / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            
            

            # Calculate the change in position from the previous frame
            delta_x = cursor_x - prev_x
            delta_y = cursor_y - prev_y

            # Move the mouse cursor based on the change in position
            pyautogui.move(delta_x, delta_y)
            pyautogui.sleep(0.05)

            # Update the previous hand position
            prev_x, prev_y = cursor_x, cursor_y

    # Display the annotated frame
    cv2.imshow('Hand Landmarks', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
