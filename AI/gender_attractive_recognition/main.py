import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import sys
import curses
import datetime
import model
import cv2
import time
import numpy as np
from imutils.video import VideoStream
import thread_pred

class face_recognition():
    def __init__(self, src):
        self.src = src
        self.faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.model = model.model()

    def gender_detection(self,nb=4):
        name = "homme - 100%"
        thread_predict_list = [thread_pred.Name(self.model,name,self.faceCascade) for i in range(nb)]
        vs = VideoStream(src=self.src).start()
        while(True):
            frame = vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
            
            if len(faces) >= 1:           
                for i in range(len(faces)):
                    (x,y,w,h) = faces[i]
                    cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)

                    if not thread_predict_list[i].is_running:
                        thread_predict_list[i].run(faces[i],frame)
                        
                    cv2.putText(frame,thread_predict_list[i].name, (x - 1, y - 1), cv2.FONT_HERSHEY_PLAIN,4,(0, 255, 0))

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        vs.stop()   

    def attractiveness_detection(self,nb=4):
        name = "homme"
        thread_predict_list = [thread_pred.Name(self.model,name,self.faceCascade) for i in range(nb)]
        vs = VideoStream(src=self.src).start()
        while(True):
            frame = vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
            
            if len(faces) >= 1:           
                for i in range(len(faces)):
                    (x,y,w,h) = faces[i]
                    cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)

                    if not thread_predict_list[i].is_running:
                        thread_predict_list[i].run(faces[i],frame)
                        
                    cv2.putText(frame,thread_predict_list[i].name, (x - 1, y - 1), cv2.FONT_HERSHEY_PLAIN,4,(0, 255, 0))

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        vs.stop()      
       

def console_menu(src):
    menu = ["Prédire le genre","Prédire la beauté","Quitter"]
    print("Bienvenue dans le dispositif de reconnaissance visuelle")
    print("\nChargement en cours...")
    face = face_recognition(src)
    rerun = ""
    while rerun != "exit":        
        os.system("clear")
        print("Bienvenue dans le dispositif de reconnaissance visuelle\n")
        print("Menu")
        while True:
            print("Sélectionner le menu désiré:")
            for i in range(len(menu)):
                print(i+1,menu[i])
            val = input()
            try: 
                val = int(val)
                if val in [i for i in range(1,len(menu)+1)]:
                    break
                else:
                    os.system("clear")
                    print("Le chiffre n'est pas dans l'intervalle demandé")

            except ValueError:
                os.system("clear")
                print("Vous n'avez pas entré de chiffre")
  
        if val == 1:
            face.gender_detection()
        elif val == 2:
            face.attractiveness_detection()
        else:
            sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        src = int(sys.argv[1])
    else:
        src = 2
    console_menu(src)
