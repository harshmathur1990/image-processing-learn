import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('raw_images/input.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = gray_image.astype(float)

fft_gray_image = np.fft.fft2(gray_image)

to_detect = cv2.imread('raw_images/to_detect.png')
gray_to_detect = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_to_detect = gray_to_detect.astype(float)

fft_gray_to_detect = np.fft.fft2(gray_to_detect)

conj_fft_gray_to_detect = np.conj(fft_gray_to_detect)

im_result = fft_gray_image * conj_fft_gray_to_detect

result = np.fft.ifft2(im_result)
abs_result = np.abs(result)
plt.subplot(121),plt.imshow(abs_result, cmap = 'gray')
plt.title('Correlation'), plt.xticks([]), plt.yticks([])
plt.show()