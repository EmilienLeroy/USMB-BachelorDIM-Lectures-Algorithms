import cv2
import numpy as np


img_bgr=cv2.imread('myimage.jpg',1)


def invert_colors_manual(input_img):
    (x,y,z)=(input_img.shape[:3])
    for x1 in range(x):
        for y1 in range(y):
            for z1 in range(z):
                new_color = 255-input_img[x1,y1,z1]
                input_img[x1,y1,z1]=new_color   
    
    return input_img

test = invert_colors_manual(img_bgr)

cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()