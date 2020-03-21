import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def signal_detector(img):
    lower_red=np.array([0,0,30])
    upper_red=np.array([10,10,255])
    lower_yellow=np.array([0,100,100])
    upper_yellow=np.array([10,255,255])
    lower_green=np.array([0,100,0])
    upper_green=np.array([50,255,50])
    mask_red=cv.inRange(img,lower_red,upper_red)
    mask_yellow=cv.inRange(img,lower_yellow,upper_yellow)
    mask_green=cv.inRange(img,lower_green,upper_green)
    if np.mean(mask_red)!=0.0:
        print('Red signal')
    elif np.mean(mask_yellow)!=0.0:
        print('Yellow signal')
    else:
        print('Green signal')
