import cv2

IMAGE_PATH = 'image.jpg'

#watermarked_img = cv2.imread(IMAGE_PATH)
#_, thresh = cv2.threshold(watermarked_img, 150, 255, cv2.THRESH_BINARY)
#
#cv2.imshow('Result', thresh)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


import cv2
import numpy as np

img = cv2.imread(IMAGE_PATH)

alpha = 2.0
beta = -160

new = alpha * img + beta
new = np.clip(new, 0, 255).astype(np.uint8)

cv2.imwrite("cleaned.png", new)

