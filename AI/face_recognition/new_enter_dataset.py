#!/usr/bin/env python 3

# Import libraries
import cv2
import os
import time
import datetime
from imutils.video import VideoStream
from alive_progress import alive_bar
import utils_model_img

# Get work directory path
directory = os.path.realpath(os.path.dirname(__file__))


from threading import Thread
class Display_image(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self,frame,faces):
        self.finish = False
        margin = 5
        image_size = 160
        x, y, w, h = faces[0]
        cropped = frame[y-margin//2:y+h+margin//2,x-margin//2:x+w+margin//2,:]
        cv2.putText(frame,f"Indice de flou: {round(cv2.Laplacian(frame, cv2.CV_64F).var())}",(20,50), cv2.FONT_HERSHEY_PLAIN,2,(0, 0, 255))

        cv2.imshow("Photo taken",cropped)
        self.finish = True



class new_entry:
    """
    A class used to handle new users
    
    Attributes
    ----------
    directory : string
        directory path where we store images
    database : database.database
        database.database object
    model_facenet : model.model
        model.model object
    faceCascade : cv2.CascadeClassifier
        cv2.CascadeClassifier object
    src : int
        video source (0 for integrated webcam)

    Methods
    -------
    webcam()
        Add new user with the webcam
    load_directory(list_split,list_name)
        Add all the users to the database thanks to the input list of names and the list of images directories
    """

    def __init__(self,database, model,face_cascade,src=2):
        """
        Parameters
        ----------
        directory : string
            directory path where we store images
        database : database.database
            database.database object
        model_facenet : model.model
            model.model object
        faceCascade : cv2.CascadeClassifier
            cv2.CascadeClassifier object
        src : int
            video source (0 for integrated webcam)
        """

        self.directory = os.path.join(directory,"saved_faces")
        self.database = database
        self.model_facenet = model
        self.faceCascade = face_cascade
        self.src = src
        
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            
    def webcam(self):
        """
        Add new user with the webcam
        """
        display = Display_image()
        one_face_found = False
        image_size = 160

        # We use the function VideoStream from the imutils.video package to improve performance as it perform 
        # parallelize computation
        stream = VideoStream(src=self.src).start()
        
        while not one_face_found:
            frame = stream.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # We detect faces
            faces = self.faceCascade.detectMultiScale(gray,
                                                     scaleFactor=1.3,
                                                     minNeighbors=5) 

            
            if len(faces) == 1: 
                try:
                    cv2.destroyAllWindows() 
                except:
                    pass      
                margin = 5
                image_size = 160
                x, y, w, h = faces[0]
                cropped = frame[y-margin//2:y+h+margin//2,x-margin//2:x+w+margin//2,:]
                cv2.putText(frame,f"Indice de flou: {round(cv2.Laplacian(frame, cv2.CV_64F).var())}",(20,50), cv2.FONT_HERSHEY_PLAIN,2,(0, 0, 255))

                cv2.imshow("Photo taken",frame)   
                cv2.imshow("Photo cropped",cropped)

                start = time.perf_counter()
                while time.perf_counter() - start < 3:                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        one_face_found = True
                        break
                    
            elif len(faces) > 1:
                cv2.putText(frame,f"More than one face found ({len(faces)} faces)",(20,50), cv2.FONT_HERSHEY_PLAIN,2,(0, 0, 255))
            else:
                cv2.putText(frame,"No faces found",(20,50), cv2.FONT_HERSHEY_PLAIN,2,(0, 0, 255))

        
        stream.stop()
        cv2.destroyAllWindows()

        if one_face_found == True:
            loop = False
            name = ""
            stream.stop()
            cv2.destroyAllWindows()
            while not loop:
                print("Enter the name: ")
                name = input().lower()    
                if not self.database.check_name(name):
                    loop = True
                else:
                    print("Cette personne existe déjà dans la base de données")

            # We preprocess image so it can be understand by the model
            image_processor = utils_model_img.image_processing(frame,self.faceCascade)

            # We save the cropped image
            cropped_image = image_processor.img_prep(faces[0])
            cv2.imwrite(f'{self.directory}/{name}.jpg', cropped_image)

            # We compute the face embeding for the image and we insert the new user to the database
            image_processor.prewhiten()
            emb = self.model_facenet.predict_emb(image_processor.img)
            self.database.update_database(name,emb)    

    
    def load_directory(self,list_split,list_name):
        """
        Add all the users to the database thanks to the input list of names and the list of images directories

        Parameters
        ----------
        list_split : list
            list of paths of all images
        list_name : list
            list of names
        """
        nbImg = 0
        erreur = 0
        i=0
        with alive_bar(len(list_split)) as bar: # progress bar
            for path, name in zip(list_split,list_name):
                img = cv2.imread(path)
                try:
                    # We preprocess all images
                    image_process = utils_model_img.image_processing(img,self.faceCascade)
                    faces = image_process.img_faces(min_size_features=0.1)
                    j=1
                    for face in faces:      
                        image_process = utils_model_img.image_processing(img,self.faceCascade)              
                        cropped_image = image_process.img_prep(face)
                        if len(faces) > 1:
                            cv2.imwrite(f'{self.directory}/{name}{j}.jpg', cropped_image)
                            self.database.update_database(f'{name}{j}',self.model_facenet.predict_emb(image_process.img))
                        else:
                            cv2.imwrite(f'{self.directory}/{name}.jpg', cropped_image)
                            self.database.update_database(name,self.model_facenet.predict_emb(image_process.img))
                        j+=1    
                except Exception as e:
                    erreur+=1
                    print("Error: ", e)
                nbImg += j
                i+=1
                bar()
        print(f"Recap: {nbImg} images enregistrées\n{i-erreur}/{i}",)
        time.sleep(4)        

        
        


    
    
