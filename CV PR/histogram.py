import cv2
from matplotlib import pyplot as plt

# 1. Read the color image
img = cv2.imread('flower n.png')

# 2. Define colors for channels and loop through them
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    # Calculate histogram for each channel
    # [img]: image, [i]: channel index, None: no mask, [256]: bins, [0,256]: range
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    
    # 3. Plot the histogram
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.title('Color Channels Histogram')
plt.xlabel('Intensity Value')
plt.ylabel('Pixel Count')
plt.show()