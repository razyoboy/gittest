import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/hela/'
files = os.listdir(folder)

total = len(files)
f, axs = plt.subplots(figsize=(15,total*6))

for i, file in enumerate(files):
    image = cv2.imread(folder + file)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = image * 15
    gray = hsv.copy()
    opening = hsv.copy()

    grayit = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    height, width = grayit.shape

    ret, thresh = cv2.threshold(grayit, 80, 255, cv2.THRESH_BINARY)

    inverted = cv2.bitwise_not(thresh)
    kernel = np.ones((50,50), np.uint8)
    opening = cv2.morphologyEx(inverted, cv2.MORPH_OPEN, kernel)

    count, hiera = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bord = np.zeros([height,width,3])

    cv2.drawContours(bord, count, -1,(0,255,0),3)

    plt.subplot(total, 2, 2 * i + 1)
    plt.title(file)
    plt.imshow(gray, cmap=plt.cm.gray)
    plt.subplot(total, 2, 2 * i + 2)
    plt.title('count = ' + str(len(count)))
    plt.imshow(opening, cmap=plt.cm.gray)

plt.show()




