import cv2 
import mediapipe . python .solutions.hands as mp_hands
import mediapipe . python .solutions . drawing_utils as drawing
import mediapipe . python . solutions . drawing_styles as drawing_styles
from google import protobuf


hands =mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5
)





cam = cv2 . VideoCapture(0)

while True :
    ret, frame = cam .read()
    if not ret :
        print ("Frame not found")
        continue


    frame = cv2 . cvtColor(frame , cv2.COLOR_BGR2RGB)
    hands_detected = hands . process(frame)
    frame = cv2 . cvtColor(frame , cv2.COLOR_RGB2BGR)


    if hands_detected .multi_hand_landmarks:
        for hand_landmarks in hands_detected.multi_hand_landmarks :
            drawing . draw_landmarks(
                frame , 
                hand_landmarks ,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style()
            )
    
    cv2 . imshow("Hands detection" , frame)
    


    if cv2 . waitKey(1) & 0xFF == ord('q'):
        break

cam . release()
cv2 . destroyAllWindows()