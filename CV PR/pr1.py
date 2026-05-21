import cv2

img = cv2.imread('image1.png')

# Line
cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 3)

# Rectangle
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 2)

# Circle
cv2.circle(img, (100, 100), 50, (0, 0, 255), -1)

# Text
cv2.putText(img, 'OpenCV', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
