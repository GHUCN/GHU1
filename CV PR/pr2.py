import cv2
import numpy as np
from matplotlib import pyplot as plt
def apply_cut(image_path,react):
    img=cv2.imread(image_path)
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    mask = np.zeros(img.shape[:2], np.uint8)


    bgd_model=np.zeros((1,65),np.float64)
    fgd_model=np.zeros((1,65),np.float64)

    cv2.grabCut(img_rgb,mask,react,bgd_model,fgd_model,5,cv2.GC_INIT_WITH_RECT)
    mask2=np.where((mask==2)|(mask==0),0,1).astype('unit8')
    img_segmented=img_rgb*mask2[:,:,np.newaxis]
    return img_rgb,img_segmented

rectangle=(50,50,400,300)
original_image,segmented_image=apply_cut('C:/Users/Admin/Desktop/CV PR/flower.png',rectangle)

plt.figure(figsize=(10,8))
plt.subplot(121),plt.imshow(original_image)
plt.title("original image") ,plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(segmented_image)
plt.title("segmented image graph cut"),plt.xticks([]),plt.yticks([])
plt.show()