#!/usr/bin/env python 3

import cv2
import numpy as np
import urllib.request
import json
import os
import time

# I- Face detection and img processing
class image_processing():
    def __init__(self,img,face_cascade,image_size=160,margin=0):
        self.img = img
        self.image_size = 160
        self.margin = 5
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.faceCascade = face_cascade
        
    def img_prep(self, face):
        (self.x, self.y, self.w, self.h) = face
        if len(self.img.shape)==3:
            cropped = self.img[self.y-self.margin//2:self.y+self.h+self.margin//2,self.x-self.margin//2:self.x+self.w+self.margin//2,:]
        else:
            cropped = self.img[self.y-self.margin//2:self.y+self.h+self.margin//2,self.x-self.margin//2:self.x+self.w+self.margin//2]
 
        new_width = 178
        new_height = 218
        dsize = (new_width, new_height)

        img = cv2.resize(cropped, dsize, interpolation = cv2.INTER_AREA)
        
        
        img_array = np.array(img) / 255.
        img_array = img_array.reshape((1,) + img_array.shape)
        
        self.img = img_array
        return cropped
        
