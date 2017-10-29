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

"""
test = invert_colors_manual(img_bgr)
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

def invert_colors_numpy(input_img):
    (x,y,z)=(input_img.shape[:3])
    myMat=np.zeros([x,y,3],dtype=int)
    myMat[::] = 255;    
    input_img[::1] = myMat[::1] - input_img[::1]
    return input_img
"""
test = invert_colors_numpy(img_bgr)
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

def invert_colors_opencv(input_img):
    b,g,r = cv2.split(input_img)
    input_img = cv2.merge((255-b,255-g,255-r)) 
    return input_img

"""
test = invert_colors_opencv(img_bgr)
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


