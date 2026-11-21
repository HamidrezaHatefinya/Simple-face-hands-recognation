import cv2
for i in range(0, 3):  # Check indexes 0, 1, 2
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera found at index {i}")
        cap.release()
    else:
        print(f"No camera at index {i}")
cv2 . destroyAllWindows()