# Import all modules
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import sys
import curses
import datetime
import cv2
import time
import numpy as np
from imutils.video import VideoStream

# Files from the project
import database
import utils_model_img
import model
import prediction
import new_enter_dataset
import thread_pred

class face_recognition:
    def __init__(self, src):
        self.src = src
        self.faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.database = database.database()
        self.model = model.model()
        self.predict = prediction.predict(self.model,self.database)
        self.entry = new_enter_dataset.new_entry(self.database,self.model,self.faceCascade,self.src)

    def new_entry(self, mode, dir_path="/home/flavien/Documents/face_recognition_inmoov/images"):
        if mode == 0:
            self.entry.webcam()
        elif os.path.exists(dir_path):
            list_img=[os.path.join(dir_path, img) for img in os.listdir(dir_path) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png")]
            list_name=[img.split('.')[0] for img in os.listdir(dir_path) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png")]
            if len(list_img)>0:
                self.entry.load_directory(list_img, list_name)
            else:
                print("Le dossier est vide")
                time.sleep(1)
        else:
            print("Dossier incorrect")
            time.sleep(1)
    
    def faces_detection(self,nb=4):
        name = "unknown"
        thread_predict_list = [thread_pred.Name(self.predict,name,self.faceCascade) for i in range(nb)]
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
    
    def face_detection(self):
        name = "unknown"
        thread_predict = thread_pred.Name(self.predict,name,self.faceCascade)
        vs = VideoStream(src=self.src).start()
        while(True):
            frame = vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

            if len(faces)==1:
                (x,y,w,h) = faces[0]
                cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)
                
                if not thread_predict.is_running:
                    thread_predict.run(faces[0],frame)
                    
                cv2.putText(frame,thread_predict.name, (x - 1, y - 1), cv2.FONT_HERSHEY_PLAIN,4,(0, 255, 0))

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        vs.stop()
    
    def predict_webcam(self):
        stream = VideoStream(src=self.src).start()
        while True:
            one_face_found = False
            start_time = datetime.datetime.now()
            elapsed_time = 0
            
            while (not one_face_found) and elapsed_time<10:
                elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
                frame = stream.read()    
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
        
                if len(faces) == 1:
                    one_face_found = True
                    print(f"Found {len(faces)} faces.")
                elif len(faces) > 1:
                    print(f"More than one face found ({len(faces)} faces)")
                else:
                    print("No faces found")
            stream.stop()
            cv2.destroyAllWindows()

            if elapsed_time>=10:
                print("No faces meeting the requirements found")    
            elif one_face_found == True:
                image_processor = utils_model_img.image_processing(frame,self.faceCascade)
                image_processor.img_prep(faces[0])  
                val = self.predict.predict_face(image_processor.img)
                if val == 0:
                    print("Le visage ne correspond à aucun visage de la base de données")
                else:
                    print(f"Bonjour {val}")
        return 0

    def predict_image(self,img_path):
        img = cv2.imread(img_path)
        image_processor = utils_model_img.image_processing(img,self.faceCascade)
        faces = image_processor.img_faces()
        image_processor.img_prep(faces[0])
        return self.predict.predict_face(image_processor.img)            

def console_menu(src):
    menu = ["Ajouter un visage à la base de données", "Ajouter des visages à partir d'un répertoire",
            "Prédire un visage avec la webcam", "Prédire un visage avec la webcam (Affichage)",
            "Prédire un visage avec une image","Prédire plusieurs visages avec la webcam (Affichage)",
            "Reset_database","Quitter"]
    print("Bienvenue dans le dispositif de reconnaissance faciale")
    print("\nChargement en cours...")
    face = face_recognition(src)
    rerun = ""
    while rerun != "exit":        
        os.system("clear")
        print("Bienvenue dans le dispositif de reconnaissance faciale\n")
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
            face.new_entry(0)
        elif val == 2:
            face.new_entry(1)
        elif val == 3:
            returned_val = face.predict_webcam()
            if returned_val == 0:
                print("Le visage ne correspond à aucun visage de la base de données")
            else:
                print(f"Bonjour {returned_val}")
        elif val == 4:
            returned_val = face.face_detection()
        elif val == 5:
            path = "temp/unnamed.jpg"
            returned_val = face.predict_image(path)
            if returned_val == 0:
                print("Le visage ne correspond à aucun visage de la base de données")
            else:
                print(f"Bonjour {returned_val}")     
        elif val == 6:
            face.faces_detection()
        elif val == 7:
            db = database.database()
            db.reset_database()
        else:
            sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        src = int(sys.argv[1])
    else:
        src = 2
    console_menu(src)
