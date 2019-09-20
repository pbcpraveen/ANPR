#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:13:51 2019

@author: praveen
"""

import os
from shutil import copyfile
os.mkdir('Train')
os.mkdir('Test')
os.mkdir('Train/Image')
os.mkdir('Train/mask')
os.mkdir('Test/Image')
os.mkdir('Test/mask')
k=0
for i in os.listdir('masks'):
    if (k<=480):
        for j in os.listdir('masks/'+i):
            src = 'masks/'+i+'/'+j
            if j[:4]=='mask':
                dest = 'Train/mask/mask_'+str(k)+'.jpg'
                copyfile(src,dest)
            else:
                dest = 'Train/Image/'+str(k)+'.jpg'
                copyfile(src,dest)
        k+=1  
    else:
        for j in os.listdir('masks/'+i):
            src = 'masks/'+i+'/'+j
            if j[:4]=='mask':
                dest = 'Test/mask/mask_'+str(k)+'.jpg'
                copyfile(src,dest)
            else:
                dest = 'Test/Image/'+str(k)+'.jpg'
                copyfile(src,dest)
        k+=1  