#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:59:44 2019

@author: praveen

"""

import cv2
def extract_ROI(image1):
    height_orginal,width_orginal=image1.shape[:2]
    
    
    #we resize the image to a standard size thus we can make sure that 
    #the plate is always positioned perfectly
    
    
    img_scaled = cv2.resize(image1, (1300, 500), interpolation = cv2.INTER_CUBIC)
    height,width=img_scaled.shape[:2]
    
    #cropping the ROI from the image
    #we assume that the plate will appear only on the bottom part of the image

    start_row,end_row = int(4*height/7),int(height)
    start_coloumn,end_coloumn =int(2*width/10) , int(9*width/10)
    ROI=img_scaled[start_row:end_row,start_coloumn:end_coloumn]
    roi_height,roi_width= ROI.shape[:2]
    scaling_factor_height=height_orginal/height
    scaling_factor_width= width_orginal/width
    
    #computing the orginal dimensions of ROI in the given image
    h=scaling_factor_height*roi_height
    w=scaling_factor_width*roi_width
    
    ROI=cv2.resize(ROI,(int(w)*2,int(h)*2),interpolation=cv2.INTER_CUBIC)
    return ROI