#!/usr/bin/env python 3

# Import libraries
import cv2
import numpy as np
import datetime

# Preprocessing
import utils_model_img


class predict:
    """
    A class used to predict people identity from an image
    
    Attributes
    ----------
    model_facenet : tensorflow.python.keras.engine.sequential.Sequential
        the CNN model used to predict face embedding from image
    database : database.database
        database object

    Methods
    -------
    predict_face(image)
        Predict the identity of the people on the image (0 if no match)
    """

    def __init__(self,model,database):
        """
        Parameters
        ----------
        model_facenet : tensorflow.python.keras.engine.sequential.Sequential
            the CNN model used to predict face embedding from image
        database : database.database
            database object
        """
        self.model_facenet = model
        self.database = database
        
    def predict_face(self,image):
        """
        Predict the identity of the people on the image (0 if no match)

        Parameters
        ----------
        image : numpy.ndarray
            preprocessed image to be accepted by the model
        
        Returns
        -------
        string
            identity of the people on the image (0 if he is not in the database)
        """
        elapsed = 0
        emb_image = self.model_facenet.predict_emb(image)
        min_dist = 100
        names,embs=self.database.get_image_emb()
        # We calculate the euclidian distance between the input image and all images from the database
        for name,emb in zip(names,embs):
            d = self.model_facenet.get_distance(emb_image,emb)



            # We search for the minimal distance 
            if(d < min_dist):
                min_dist = d
                identity = name

        # If the distance is lower than a threshold sets arbitrary we return the linked identity
        if min_dist < 13:
            return identity
        else:            
            return 0
