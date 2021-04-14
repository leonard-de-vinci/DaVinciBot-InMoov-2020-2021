from imutils.video import VideoStream
import cv2
import numpy as np
import model

model = model.model()

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
vs = VideoStream(src=2).start()
name = "homme"
while(True):
    frame = vs.read()

    faces = faceCascade.detectMultiScale(frame,scaleFactor=1.3,minNeighbors=5)

    margin = 5
    img_width = 178
    img_height = 218
    x=0
    y=0
    if len(faces) >= 1:   
        img = frame.copy()        
        (x,y,w,h) = faces[0]
        if len(img.shape)==3:
            cropped = img[y-margin//2:y+h+margin//2,x-margin//2:x+w+margin//2,:]
        else:
            cropped = img[y-margin//2:y+h+margin//2,x-margin//2:x+w+margin//2]
            
        img = cv2.resize(cropped, (img_width,img_height))
        img = np.array(img)
        image = np.zeros((1, img_height,img_width, 3))
        image[0,:,:,:] = img
        img = img/255.0
        r = model.predict(img)
        print(r)
        if r == 0:
            name = "femme"
        else:
            name = "homme"

    cv2.putText(frame,name, (x - 1, y - 1), cv2.FONT_HERSHEY_PLAIN,4,(0, 255, 0))
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
vs.stop()   