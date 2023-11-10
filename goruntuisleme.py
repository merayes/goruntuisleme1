import cv2

import matplotlib.pyplot as plt

import numpy as np

image_path = r'''C:\Users\USER\Desktop\images.jpg'''

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

histogram = [0] * 256
for row in img:
    for pixel_value in row:
        histogram[pixel_value] += 1

plt.bar(range(256), histogram, color='gray', alpha=0.7)
plt.title('Gri Seviye Histogram')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.show()
