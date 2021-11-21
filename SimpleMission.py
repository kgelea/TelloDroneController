# -*- coding: utf-8 -*-
# This program will make the drone take off, and take a picture in every direcetion
from djitellopy import Tello
import cv2, math, time

#%% Estabilish connection
tello = Tello()
tello.connect()

#%% Turn on video
tello.streamon()
frame_read = tello.get_frame_read()


#%% Do some basic commands
# This will make tello
images = []

tello.takeoff()

for i in range(4):
    time.sleep(6) # wait 10 seconds
    image = tello.get_frame_read().frame
    cv2
    tello.rotate_clockwise(90)

tello.land()

#%% 
cv2.imshow('drone', image)
cv2.waitKey(0)
