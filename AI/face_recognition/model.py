#!/usr/bin/env python 3

# Avoid log printing
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

# Import libraries
from tensorflow.keras.models import load_model
import numpy as np
import os

# Get the model path
path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "facenet_keras.h5")

class model:
    """
    A class used to import the FaceNet model from google

    FaceNet learns a mapping from face images to a compact Euclidean space where distances
    directly correspond to a measure of face similarity.

    On the Labeled Faces in the Wild (LFW) dataset, their system achieves a new record accuracy of 99.63%. 
    On YouTube Faces DB it achieves 95.12%.

    More details : https://arxiv.org/pdf/1503.03832.pdf

    Attributes
    ----------
    model : tensorflow.python.keras.engine.sequential.Sequential
        CNN model used to extract the  face embedding from image

    Methods
    -------
    predict_emb(image)
        Predict the face embedding of the input image
    get_distance(emb_image,image)
        Compute the euclidian distance between the face embedding of the unknown people image
        and an image from the database
    """

    def __init__(self):
        """
        Parameters
        ----------
        model : tensorflow.python.keras.engine.sequential.Sequential
            the CNN model use to predict face embedding from image
        """
        self.model = load_model(path)
    
    def predict_emb(self,image):
        """
        Predict the face embedding of the input image

        Parameters
        ----------
        image : numpy.ndarray
            image preprocess to be accepted by the model
        
        Returns
        -------
        numpy.ndarray
            face embedding containing 128 element that represents high-quality features from the face
        """
        return self.model.predict(image)
    
    def get_distance(self, emb_unknown_image, emb):
        """
        Compute the euclidian distance between the faceembedding of the unknown people image 
        and an image from the database

        Parameters
        ----------
        emb_image : numpy.ndarray
            The face embedding of the unknown people image 
        emb : numpy.ndarray
            The face embedding of an image from the database 
        
        Returns
        -------
        float
            distance between the two face embeddings
        """
        return np.linalg.norm(emb_unknown_image - emb)
    
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
        emb_image = self.predict_emb(image)
        min_dist = 100

        # We calculate the euclidian distance between the input image and all images from the database
        for name,emb in self.database.database.items():
            d = self.model_facenet.get_distance(emb_image,emb)
            print(d, name)
            # We search for the minimal distance 
            if(d < min_dist):
                min_dist = d
                identity = name

        # If the distance is lower than a threshold sets arbitrary we return the linked identity
        if min_dist < 13:
            return identity
        else:            
            return 0