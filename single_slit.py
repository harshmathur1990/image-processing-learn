import numpy as np
import cv2
import pylab as py
import math
from matplotlib import pyplot as plt

grid = np.zeros((4000, 4000), np.float)

for y in range(190,210):
    for x in range(180, 219):
        grid[x][y] = 255

D1 = np.fft.fft2(grid)
D2 = np.fft.fftshift(D1)

magnitude_spectrum = np.abs(D2)
plt.subplot(121),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()