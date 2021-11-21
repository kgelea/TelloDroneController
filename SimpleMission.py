# -*- coding: utf-8 -*-
# This program will make the drone take off, and take a picture in every direcetion
from tello import Tello
import cv2, math, time

#%% Estabilish connection
tello = Tello()
tello.connect()

#%% Turn on video
tello.streamon()
frame_read = tello.get_frame_read()
cv2.imshow("drone", frame_read.frame)


#%% Do some basic commands
# This will make tello
tello.streamon()

images = []

tello.takeoff()

for i in range(4):
    time.sleep(20) # wait 10 seconds
    image = tello.get_frame_read().frame
    images.append(image)
    tello.rotate_clockwise(90)

tello.land()

