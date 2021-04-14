#!/usr/bin/env python 3
import sys
from threading import Thread
from utils_model_img import image_processing

class Name(Thread):
    def __init__(self, model,name,faceCascade):
        Thread.__init__(self)
        self.model = model
        self.name = name
        self.faceCascade = faceCascade
        self.is_running = False

    def run(self,faces,frame):
        self.is_running = True
        image_processor = image_processing(frame,self.faceCascade)
        image_processor.img_prep(faces)       
        self.name = self.model.predict(image_processor.img)
        self.is_running=False
        
