#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:54:13 2019

@author: praveen
"""


import cv2

import numpy as np
from keras.preprocessing import image


def plate_predict(classifier,img):
    test_image = cv2.resize(img,(100,30))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    if result[0][0] ==1 :
      return 1
    else:
      return 0
