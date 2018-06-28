import numpy as np
import math
from matplotlib import pyplot as plt

grid = np.zeros((300, 300), np.float)

for y in range(0, 300):
    for x in range(0, 300):
        grid[x][y] = (1 + math.cos(2 * np.pi * y  * 10 / 101)) * 255

D1 = np.fft.fft2(grid)
D2 = np.fft.fftshift(D1)

magnitude_spectrum = np.abs(D2)
plt.subplot(121),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()