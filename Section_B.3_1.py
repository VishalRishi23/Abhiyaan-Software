import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def canny_edge_detector(image):
    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray_image,(5,5),0)
    canny=cv.Canny(blur,50,150)
    return canny
def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([[(0,240),(700,240),(700,397),(0,397)]])
    mask=np.zeros_like(image)
    cv.fillPoly(mask,polygons,255)
    masked_image=cv.bitwise_and(image,mask)
    return masked_image
def create_coordinates(image,line_parameters):
    slope,intercept=line_parameters
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope)
    x2=int((y2-intercept)/slope)
    return np.array([x1,y1,x2,y2])
def average_slope_intercept(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        slope=parameters[0]
        intercept=parameters[1]
        if slope<0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average=np.average(left_fit,axis=0)
    right_fit_average=np.average(right_fit,axis=0)
    left_line= create_coordinates(image,left_fit_average)
    right_line= create_coordinates(image,right_fit_average)
    return np.array([left_line,right_line])
def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for x1,y1,x2,y2 in lines:
            cv.line(line_image,(x1,y1),(x2,y2),(0,0,255),2)
    return line_image
img=cv.imread('Lane.jpg')
canny_image=canny_edge_detector(img)
cropped_image=region_of_interest(canny_image)
lines=cv.HoughLinesP(cropped_image,1,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
averaged_lines=average_slope_intercept(img,lines)
line_image=display_lines(img,averaged_lines)
combo_image=cv.addWeighted(img,1.,line_image,1,1)
cv.imwrite('Lane_transform.jpg',combo_image)
