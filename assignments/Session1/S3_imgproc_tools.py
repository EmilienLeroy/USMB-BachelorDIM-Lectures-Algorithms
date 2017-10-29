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

def threshold_image_manual(input_img):
    (x,y,z)=(input_img.shape[:3])
    for x1 in range(x):
        for y1 in range(y):
            for z1 in range(z):
                if input_img[x1,y1,z1] > 128:
                    new_color = 255
                    input_img[x1,y1]=new_color  
                   
                else:
                    new_color = 0
                    input_img[x1,y1]=new_color   
            
    return input_img 

 
"""              
test = threshold_image_manual(img_bgr)                
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
def threshold_image_numpy(input_img):
    input_img = cv2.cvtColor( input_img, cv2.COLOR_RGB2GRAY )
    input_img[input_img > 128] = 255
    input_img[input_img < 128] = 0
    return input_img

"""
test = threshold_image_numpy(img_bgr)            
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()    
"""

def threshold_colors_opencv(v):
    input_img = cv2.cvtColor( input_img, cv2.COLOR_RGB2GRAY )
    ret2,th2 = cv2.threshold(input_img[::1],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)    
    return th2

"""
test = threshold_colors_opencv(img_bgr)            
cv2.imshow("BGR image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""




