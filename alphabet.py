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
import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Flatten, Dense
import pyglet
def Convert(string): 
    li = list(string.split(",")) 
    return li


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

import operator
cap = cv2.VideoCapture(1)
st = ""
no_of_times = 0
platform = pyglet.window.get_platform()
display = platform.get_default_display()
for screen in display.get_screens():
    #print(screen)
    continue
width, height = screen.width, screen.height



while True:
    try:
        ret, frame1 = cap.read()
        cv2.imshow('f',frame1)
        frame2 = frame1
        frame_org = cv2.resize(frame2,(width,height))
        frame2 = frame_org
        cv2.imshow('img',frame_org)
        cv2.imshow('imshow',frame2)
        #cv2.imshow('cvt2',frame2)
        frame = frame2.copy()
        frame_new= frame2.copy()
        #cv2.imshow('frame',frame2)
        th1 = 165     
        img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gary',img2)
        
        ret, cvt= cv2.threshold(img2, th1, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow('cvt1',cvt)
        
        kernel = np.ones((5,5), np.uint8) 
        cvt = cv2.dilate(cvt, kernel, iterations=1) 
       # cv2.imshow('cvt',cvt)
        contours, hierarchy = cv2.findContours(cvt,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        thisdict = {}
        cv2.imshow('cvt',cvt)
        
        flag=0
        noted_y=0
        mylist = []
        for c in contours:
            (x, y, w, h)= cv2.boundingRect(c)
            if (w>20) or (h>20):
                mylist.append((x,y,w,h))
       
        
        th2 = 75 #change thresholding of every contour
        for i in range(0, len(mylist)):
            x = mylist[i][0]
            y = mylist[i][1]
            w = mylist[i][2]
            h = mylist[i][3]
            #cv2.rectangle(frame2,(x,y),(x+w,y+h), (255,0, 255), 2)
        
            
            cv2.rectangle(frame2,(x,y),(x+w,y+h), (0,0, 255), 2)
            img1 = cvt[y-10:y+h+10, x-10:x+w+10]
            gray = img1
            ret, gray = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)
        
            try:
                im = cv2.resize(gray, (28,28))
                ar = np.ones((28,28,3),dtype = np.uint8)
                ar[:,:,0] = im
                ar[:,:,1] = im
                ar[:,:,2] = im
                #cv2.imshow('img',gray)
                ar = np.array(ar).reshape((28,28,3))
                cv2.imshow('input',ar)
                ar = np.expand_dims(ar, axis=0)
                prediction = model.predict(ar)[0].tolist()
                # of class labels
                u = prediction.index(max(prediction))
                j = chr(65+u)
                #printing prediction
                cv2.putText(frame2, j, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)
                thisdict[x]= str(j)
            except:
                d=0
            
            sort = sorted(thisdict.items(), key=operator.itemgetter(0))
            s = ""
        cv2.imshow('myframe',frame2)
        
        for x in range(0,len(sort)):
            s=s+str(sort[x][1])
            #cv2.putText(frame2, s, (100,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)  

        
        cv2.imshow('myframe',frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break
    except:
        pass
