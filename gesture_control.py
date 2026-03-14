import cv2 #captures live image processing, computer vision, and deep learning
import mediapipe as mp #google ai library for real time hand tracking, face detection, and pose estimation
import pyautogui #for automating keyboard and mouse actions
mp_hands = mp.solutions.hands #mediapipe's hands module which detects and tracks hand landmarks in real-time

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) #creates and instance of mediapipe's hands detector (hands) and will detect and track hands in video input
#minimum confidence- confidence required to detect and track a hand
#higher confidence reduces false detections, improving accuracy

mp_draw = mp.solutions.drawing_utils #draw hand landmarks on the image
#counts the number of extended fingers in a detected hand using MP
#returns a count of extended fingers
#doesn't include the thumb
def count_fingers(hand_landmarks): 
    finger_tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                   mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                   mp_hands.HandLandmark.RING_FINGER_TIP,
                   mp_hands.HandLandmark.PINKY_TIP]
    finger_mcp = [mp_hands.HandLandmark.INDEX_FINGER_MCP,
                  mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                  mp_hands.HandLandmark.RING_FINGER_MCP,
                  mp_hands.HandLandmark.PINKY_MCP]

    count = 0
    for tip, mcp in zip(finger_tips, finger_mcp):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[mcp].y:
            count += 1
    return count 

import os
def perform_action(finger_count):
    if finger_count == 1:
        # Minimize all windows (Windows)
        pyautogui.hotkey('win', 'd')
    elif finger_count == 2:
        # Open Chrome
        os.system("start chrome")
    elif finger_count == 3:
        # Example: Open File Explorer
        os.system("notepad")
    elif finger_count == 4:
        # Example: Lock the screen (Windows)
        pyautogui.hotkey('win', 'l')
    elif finger_count == 5:
        # Example: Open Task Manager (Windows)
        pyautogui.hotkey('ctrl', 'shift', 'esc')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame and find hands
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            finger_count = count_fingers(hand_landmarks)
            perform_action(finger_count)

    cv2.imshow('Hand Gesture Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()