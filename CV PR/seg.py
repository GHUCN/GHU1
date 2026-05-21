import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_cut(image_path, rect):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found")

    mask = np.zeros(img.shape[:2], np.uint8)

    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Apply GrabCut on BGR image
    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    img_segmented = img * mask2[:, :, np.newaxis]

    # Convert to RGB for plotting
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_segmented_rgb = cv2.cvtColor(img_segmented, cv2.COLOR_BGR2RGB)

    return img_rgb, img_segmented_rgb


rectangle = (50, 50, 400, 300)
original_image, segmented_image = apply_cut(
    'C:/Users/Admin/Desktop/CV PR/lion2.jpg',
    rectangle
)

plt.figure(figsize=(10, 8))

plt.subplot(121)
plt.imshow(original_image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(122)
plt.imshow(segmented_image)
plt.title("Segmented Image (GrabCut)")
plt.axis("off")

plt.show()
