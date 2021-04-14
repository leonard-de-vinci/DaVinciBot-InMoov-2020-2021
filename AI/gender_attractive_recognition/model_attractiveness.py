#!/usr/bin/env python 3

# Avoid log printing
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

# Import libraries
from tensorflow.keras.models import load_model
import numpy as np
import os

path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "attractive_net.h5")

class model():
    def __init__(self):
        self.model = load_model(path)
    
    # II- Feature extraction
    def predict(self,image):
        retour = self.model.predict(image)[0]
        if retour[0] > 0.5:
            return "Femme - " + str(round(retour[0]*100,2)) + "%"
        else:
            return "Homme - " + str(round(retour[1]*100,2)) + "%"