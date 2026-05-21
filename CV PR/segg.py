import cv2
import numpy as np
image=cv2.imread("C:/Users/Admin/Desktop/CV PR/image.png")

image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

segmented_image=cv2.pyrMeanShiftFiltering(image, sp=20,sr=30)

segmented_image_bgr=cv2.cvtColor(segmented_image,cv2.COLOR_BGR2RGB)

cv2.imshow("origanal Image", cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
cv2.imshow("Mean Shift Segmention", segmented_image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()