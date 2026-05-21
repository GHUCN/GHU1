import cv2

image =cv2.imread("C:/Users/Admin/Desktop/CV PR/flower.png")
cv2.imshow("origanal image",image)
cv2.waitKey(0)

image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",image_grey)
cv2.waitKey(0)

ret, thresh=cv2.threshold(image_grey, 150, 255,cv2.THRESH_BINARY)
cv2.imshow("Binary Image",thresh)
cv2.waitKey(0)

contours, heirarchy=cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
image_copy=image.copy()

cv2.drawContours(image_copy, contours, -1, (0,0,255),2, cv2.LINE_AA)
cv2.imshow("contour Image",image_copy)
cv2.waitKey(0)