#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:40:43 2019

@author: praveen
"""
import cv2
import numpy as np
import os
for i in os.listdir('dataset/train/negative '):
    img = cv2.imread('dataset/train/negative /'+i,0)
    ret,img = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
    cv2.imshow('data',img)
    cv2.imwrite('dataset/train/negative /'+i,img)
    cv2.waitKey(0)
cv2.destroyAllWindows()