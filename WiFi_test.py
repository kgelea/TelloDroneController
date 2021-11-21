# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:40:44 2021

@author: Daniel Kuknyo
"""

# -*- coding: utf-8 -*-
# This program will make the drone take off, and take a picture in every direcetion
from djitellopy import Tello
import cv2, math, time
import matplotlib.pyplot as plt

#%% Estabilish connection
tello = Tello()

#%%
tello.connect()

#%% Turn on video
tello.streamon()

#%%
images = []

for i in range(10):
    frame_read = tello.get_frame_read()
    print('done', i)
    images.append(frame_read.frame)
    
    
#%% 
tello.streamoff()

#%%

cv2.imshow("drone", frame_read.frame)
cv2.waitKey(0)
