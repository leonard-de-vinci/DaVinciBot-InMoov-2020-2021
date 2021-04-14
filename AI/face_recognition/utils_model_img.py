#!/usr/bin/env python 3

# Import libraries
import cv2
import numpy as np
import urllib.request
import json
import os

# Face detection and img processing
class image_processing:
    """
    A class 
    
    Attributes
    ----------
    img : numpy.ndarray
        input image to preprocess
    image_size : int
        model trained on 160x160 pixels because it's the best compromise (https://arxiv.org/pdf/1503.03832.pdf)
    margin : int 
        margin around the found face
    x : int
        abscissa of the point in the up left corner
    y : int
        ordinate of the point in the up left corner
    w : int
        width of the image
    h : int
        height of the image
    faceCascade : cv2.CascadeClassifier
        cascade object use to localize faces on an image

    Methods
    -------
    img_faces(min_size_features=0.2)
        Detect faces on the input image
    img_prep(face)
        Cut and reshape the image to meet the model requirements
    prewhiten()
        Preprocess the image in the same way that dataset used to train the model
    """

    def __init__(self,img,face_cascade,image_size=160,margin=0):
        """
        Parameters
        ----------
        img : numpy.ndarray
            input image to preprocess
        image_size : int
            model trained on 160x160 pixels because it's the best compromise (https://arxiv.org/pdf/1503.03832.pdf)
        margin : int 
            margin around the found face
        x : int
            abscissa of the point in the up left corner
        y : int
            ordinate of the point in the up left corner
        w : int
            width of the image
        h : int
            height of the image
        faceCascade : cv2.CascadeClassifier
             cascade object use to localize faces on an image
        """
        self.img = img
        self.image_size = 160
        self.margin = 5
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.faceCascade = face_cascade
    
    def img_faces(self,min_size_features=0.2):
        """
        Detect faces on the input image

        Parameters
        ----------
        min_size_features : float
            minimal size of rectangles to consider to be a face (between 0 and 1)
        
        Returns
        -------
        list
            list of array containing for each face found on the input image, 4 points delimiting a rectangle around them
        """
        faces = self.faceCascade.detectMultiScale(self.img,
                                             scaleFactor=1.1,
                                             minNeighbors=3,
                                             minSize=(int(self.img.shape[0]*min_size_features), 
                                                      int(self.img.shape[1]*min_size_features)))
        return faces
    
    def img_prep(self, face):
        """
        Cut and reshape the image to meet the model requirements

        Parameters
        ----------
        face : numpy.ndarray
            array containing 4 points delimiting a rectangle around the face found on the input image
        
        Returns
        -------
        numpy.ndarray
            cropped image
        """
        # We get the four points delimiting the face
        (self.x, self.y, self.w, self.h) = face

        # We cropped the image depending on his shape
        if len(self.img.shape)==3:
            cropped = self.img[self.y-self.margin//2:self.y+self.h+self.margin//2,self.x-self.margin//2:self.x+self.w+self.margin//2,:]
        else:
            cropped = self.img[self.y-self.margin//2:self.y+self.h+self.margin//2,self.x-self.margin//2:self.x+self.w+self.margin//2]
            
        self.img = cv2.resize(cropped, (self.image_size, self.image_size))
        self.img = np.array(self.img)

        # We applied some operations the image
        image = np.zeros((1, self.image_size, self.image_size, 3))
        self.prewhiten()
        image[0,:,:,:] = self.img
        self.img = image
        return cropped
        
    def prewhiten(self):
        """
        Preprocess the image in the same way that dataset used to train the model
        """
        mean = np.mean(self.img)
        std = np.std(self.img)
        std_adj = np.maximum(std, 1.0/np.sqrt(self.img.size))
        self.img = np.multiply(np.subtract(self.img, mean), 1/std_adj)
        

def all_faces_names(directory):
    """
    Extract from a directory all names and paths of contained images 

    Parameters
    ----------
    directory : string
        directory used
        
    Returns
    -------
    list
        list of paths for all images in the input directory 
    list
        list of names extracted from images names
    """
    extension = ["jpg","jpeg","bmp","png"]
    liste = os.listdir(directory)
    list_split = []
    list_name = []
    for element in liste:
        split = element.split(".")
        # We verify that the file is an image
        if len(split)>1 and split[-1] in extension: 
            list_split.append(directory+"/"+element)
            split.pop()
            # We add the names to the list
            list_name.append('.'.join(split).title())
    return list_split,list_name
