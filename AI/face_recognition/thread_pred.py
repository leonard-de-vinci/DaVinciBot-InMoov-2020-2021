#!/usr/bin/env python 3

# Import libraries
import sys
from threading import Thread
from utils_model_img import image_processing

class Name(Thread):
    """
    A class used to parallelize calculations in order to use the model in realtime
    
    Attributes
    ----------
    predict : prediction.predict
        prediction object use to get the identity of a people on a frame
    name : string
        people name
    faceCascade : cv2.CascadeClassifier
        cascade object use to localize faces on an image
    is_running : bool
        boolean variable that indicates whether the calculations are completed

    Methods
    -------
    run(face, frame)
        Predict the identity from the input frame
    """

    def __init__(self,predict,name,faceCascade):
        """
        Parameters
        ----------
        predict : prediction.predict
            prediction object use to get the identity of a people on a frame
        name : string
            identity name
        faceCascade : cv2.CascadeClassifier
             cascade object use to localize faces on an image
        is_running : bool
            boolean variable that indicates whether the calculations are completed
        """
        Thread.__init__(self)
        self.predict = predict
        self.name = name
        self.faceCascade = faceCascade
        self.is_running = False

    def run(self,face,frame):
        """
        Predict the identity from the input frame

        Parameters
        ----------
        face : numpy.ndarray
            array containing 4 points delimiting a rectangle around the face found on the input image
        frame : numpy.ndarray
            image
        """
        self.is_running = True
        # Preprocess the image
        image_processor = image_processing(frame,self.faceCascade)
        image_processor.img_prep(face)       
        # Predict the identity
        self.name = self.predict.predict_face(image_processor.img)
        if self.name == 0 or self.name == "0":
            self.name = "Unknown"
        self.is_running=False
        
