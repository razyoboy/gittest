import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/'
question = folder + 'apples02.jpg'

image = cv2.imread(question)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

out = image.copy()
height, width, depth = out.shape
h, s, v = cv2.split(out)
h += 55

greenlantern = cv2.merge([h,s,v])
out = cv2.cvtColor(greenlantern, cv2.COLOR_HSV2BGR)

f, axs = plt.subplots(figsize=(15,15))
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(out)
plt.show()