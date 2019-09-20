#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:55:28 2019

@author: praveen
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:30:21 2019

@author: praveen
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:27:11 2019

@author: praveen
"""

import cv2
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Flatten, Dense
import pyglet
def Convert(string): 
    li = list(string.split(",")) 
    return li
import os

def create_model():
    model = Sequential()
    model.add(Convolution2D(16, 5, 5, activation='relu', input_shape=(28,28, 3)))
    model.add(MaxPooling2D(2, 2))

    model.add(Convolution2D(32, 5, 5, activation='relu'))
    model.add(MaxPooling2D(2, 2))

    model.add(Flatten())
    model.add(Dense(1000, activation='relu'))

    model.add(Dense(26, activation='softmax'))
    return model

model = create_model()
model.load_weights('./OCR_model.h5')

for i in os.listdir('character'):
    im = cv2.imread('character/'+i)
    im = cv2.resize(im, (28,28))
    ar = im
    #cv2.imshow('img',gray)

    #cv2.imshow('input',ar)
    ar = np.expand_dims(ar, axis=0)
    prediction = model.predict(ar)[0].tolist()
    # of class labels
    u = prediction.index(max(prediction))
    j = chr(65+u)
    #printing prediction
    print(j)
