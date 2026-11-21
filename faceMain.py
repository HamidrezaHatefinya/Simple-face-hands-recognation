import cv2
import datetime


#region(load face)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#endregion

#region(open video)
cap = cv2.VideoCapture(0)  


while True:
    ret, frame = cap.read()

    mytime = datetime .datetime . now()                #data on top left
    qurrentTime = mytime . strftime("%H:%M:%S")
    cv2 . putText (frame , str(qurrentTime) , (50,50) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,255) , 1 )   
    cv2 . rectangle (frame , (20,5) , (350,120) , (255,0,0) , 2)
    cv2 . line(frame , (50,65) , (320,65) , (200,255,0) , 2)

    
    if not ret:                          #frame check!!!
        print("Frame not captured!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    
    for (x, y, w, h) in faces:             #box drawing around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2 . putText (frame , "Person detected" , (50,100) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,255) , 1 )

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):          #exit key is (q)
         break
    

#endregion


#region (destroy)
cap . release()
cv2 . destroyAllWindows()
#endregion
