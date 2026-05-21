import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.png")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
b, g, r = cv2.split(image)
cv2.imshow("BGR", image)
# cv2.imshow("HSV", hsv)
zeros = np.zeros_like(b)
blue_img  = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img   = cv2.merge([zeros, zeros, r])
cv2.imshow("Blue", blue_img)
cv2.imshow("green", green_img)
cv2.imshow("red", red_img)
cv2.waitKey(0)