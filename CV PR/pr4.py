import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("flower bw.png")
hist, bins = np.histogram(img.flatten(), 256, [0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()

plt.plot(cdf_normalized, color = 'r')
plt.hist(img.flatten(), 256,[0,256], color='g')
plt.xlim([0,256])
plt.ylabel('Pixel Count')
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()