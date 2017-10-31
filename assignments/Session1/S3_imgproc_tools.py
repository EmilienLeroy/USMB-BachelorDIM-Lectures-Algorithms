# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:48:09 2017
@brief a set of function able to work with image
@author: leroyem
"""
#import libs
import cv2
import numpy as np

#image test
img_bgr=cv2.imread('myimage.jpg',1)

## invert_colors_manual(input_img)
#  @param input_img; image who will be invert
#  @details function able to invert the color of a image
def invert_colors_manual(input_img):
    #Get the 3 dimension of the image
    # z is the color (Red,Blue,Green)
    (x,y,z)=(input_img.shape[:3])
    
    #Crossing all the image
    for x1 in range(x):
        for y1 in range(y):
            for z1 in range(z):
                #invert the color
                new_color = 255-input_img[x1,y1,z1]
                input_img[x1,y1,z1]=new_color   
                
    # @return the new image
    return input_img

"""
#Testing invert_colors_manual function
test = invert_colors_manual(img_bgr)
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

## invert_colors_numpy(input_img)
#  @param input_img; image who will be invert
#  @details function able to invert the color of a image
def invert_colors_numpy(input_img):
    #Get the 3 dimension of the image
    # z is the color (Red,Blue,Green)    
    (x,y,z)=(input_img.shape[:3])
    
    #Create an array with the image size
    myMat=np.zeros([x,y,3],dtype=int)
    
    #Fill the array with the value 255
    myMat[::] = 255;
    
    #invert the color of the image
    input_img[::1] = myMat[::1] - input_img[::1]
    
    # @return the new image
    return input_img

"""
#Testing invert_colors_numpy function
test = invert_colors_numpy(img_bgr)
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

## invert_colors_opencv(input_img)
#  @param input_img; image who will be invert
#  @details function able to invert the color of a image
def invert_colors_opencv(input_img):
    #split the image in 3 layers
    b,g,r = cv2.split(input_img)
    
    #invert each layers and merge in one image
    input_img = cv2.merge((255-b,255-g,255-r)) 
    
    # @return the new image
    return input_img

"""
#Testing invert_colors_opencv function
test = invert_colors_opencv(img_bgr)
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

## threshold_image_manual(input_img)
#  @param input_img; image who will be threshold
#  @details function able to threshold an image
def threshold_image_manual(input_img):
    #Get the 3 dimension of the image
    # z is the color (Red,Blue,Green)
    (x,y,z)=(input_img.shape[:3])
    
    #Crossing all the image
    for x1 in range(x):
        for y1 in range(y):
            for z1 in range(z):
                #if the pixel is bigger than 128
                if input_img[x1,y1,z1] > 128:
                    #the color of the pixel is with
                    new_color = 255
                    input_img[x1,y1]=new_color
                    
                #else the pixel is black
                else:
                    new_color = 0
                    input_img[x1,y1]=new_color   
            
    # @return the new image
    return input_img 

 
"""
#Testing threshold_image_manual function
test = threshold_image_manual(img_bgr)                
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

## threshold_image_numpy(input_img)
#  @param input_img; image who will be threshold
#  @details function able to threshold an image
def threshold_image_numpy(input_img):
    #change the image in gray
    input_img = cv2.cvtColor( input_img, cv2.COLOR_RGB2GRAY )
    
    #if input_img[pixel]>128 
    #pixel is white
    input_img[input_img > 128] = 255
    
    #else 
    #pixel is blacl    
    input_img[input_img < 128] = 0
    
    # @return the new image
    return input_img

"""
#Testing threshold_image_numpy function
test = threshold_image_numpy(img_bgr)            
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()    
"""

## threshold_colors_opencv(input_img)
#  @param input_img; image who will be threshold
#  @details function able to threshold an image
def threshold_colors_opencv(input_img):
    #change the image in gray
    input_img = cv2.cvtColor( input_img, cv2.COLOR_RGB2GRAY )
    #opencv function to threshold image
    ret2,th2 = cv2.threshold(input_img[::1],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)    
    # @return the new image
    return th2

"""
#Testing threshold_colors_opencv function
test = threshold_colors_opencv(img_bgr)            
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""



