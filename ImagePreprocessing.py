#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:11:09 2019

@author: praveen
"""
import cv2
import numpy as np
def preprocess(ROI):
    # Converting the image to the grayscale
    gray1 = cv2.cvtColor(ROI,cv2.COLOR_BGR2GRAY)
    
    
    # to remove the unwnated noises in the surroundings the image is blurred with a kernel size of 5x5 
    bright=np.ones((3,3),dtype='uint8')*(1/9) #kernel matrix
    gray=cv2.filter2D(gray1,-1,bright)
    
    # Finding Canny edges
    #canny edge algorithm will plot all the possible contours in the pre processed image
    edged = cv2.Canny(gray, 5, 100)
    
    # to remove unwanted minor edges morphological operation is done on the cannied image.
    kernel = np.ones((3,3), np.uint8)
    morph = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    # MORPH_OPEN : dilate and erode
    # MORPH_CLOSE: Erode and Dilate
    return morph