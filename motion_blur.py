import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy
from scipy import signal


grid = np.zeros((400, 400), np.float)


for y in range(200, 240):
    grid[200][y] = 255.0
    grid[201][y] = 255.0
    grid[202][y] = 255.0
    grid[203][y] = 255.0

cropped_grid = grid[150:251, 170:271]


image = cv2.imread('raw_images/dog.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = gray_image.astype(float)

plt.subplot(231),plt.imshow(gray_image, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])


plt.subplot(232),plt.imshow(grid, cmap = 'gray')
plt.title('Original Line'), plt.xticks([]), plt.yticks([])

plt.subplot(233),plt.imshow(cropped_grid, cmap = 'gray')
plt.title('Cropped Line'), plt.xticks([]), plt.yticks([])


convolution =  scipy.signal.convolve2d(gray_image, cropped_grid)

plt.subplot(234),plt.imshow(convolution, cmap = 'gray')
plt.title('Motion Blur'), plt.xticks([]), plt.yticks([])
# plt.show()

fft_convolution = np.fft.fft2(convolution)

plt.subplot(235),plt.imshow(np.abs(np.fft.fftshift(fft_convolution)), cmap = 'gray')
plt.title('FFT of Blurred Image'), plt.xticks([]), plt.yticks([])

sinc = np.fft.fft2(grid)

division_result = np.divide(fft_convolution, sinc)

# plt.subplot(235),plt.imshow(np.abs(np.fft.fftshift(sinc)), cmap = 'gray')
# plt.title('Sinc Function'), plt.xticks([]), plt.yticks([])

ifft_division_result = np.fft.ifft2(division_result)

plt.subplot(236),plt.imshow(np.abs(np.fft.fftshift(ifft_division_result)), cmap = 'gray')
plt.title('After removing Blur'), plt.xticks([]), plt.yticks([])
plt.show()
