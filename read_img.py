# Python program to read image using OpenCV
  
# importing OpenCV(cv2) module
import cv2
import numpy as np
from numpy import load, save

mask = load ('painter075_mask.npy')
print (mask.shape)
  
# Save image in set directory
# Read RGB image
img = cv2.imread('painter075.png') 
#print (img.shape)
#print (img[45][68])
#new_img = np.zeros((1088,2048,3),np.uint8)
new_img = cv2.imread('output_z3.0_painter075.png')
#print (new_img[45][68])  
# Output img with window name as 'image'
#cv2.imshow('image', img) 
#cv2.imshow('image1', new_img) 
# Maintain output window utill
# user presses a key

#np.set_printoptions(threshold=np.inf)
index=np.where(mask == True)
count=0    
for i in index[0]: 
    count=count+1   
    if i==14:
        new_img [index[1][count-1]][index[2][count-1]]= img [index[1][count-1]][index[2][count-1]]
#instance = np.where(index[0]==0)
#print (instance)
#print (count)
cv2.imshow('image1', new_img) 
cv2.imwrite('refocused_painterv2.png', new_img)
cv2.waitKey(0)        
  
# Destroying present windows on screen
cv2.destroyAllWindows() 