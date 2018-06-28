import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


def do():
    grid = np.zeros((300, 300), np.float)

    for y in range(0, 300):
        for x in range(0, 300):
            grid[x][y] = (1 + math.cos(2 * np.pi * y  * 10 / 101)) * 255

    cv2.imwrite('raw_images/sinusoidal_grating.png', grid)

    fft_grid = np.fft.fft2(grid)
    fftshift_fft_grid = np.fft.fftshift(fft_grid)

    center_x, center_y = 149, 149

    for i in range(0, 300):
        for j in range(0, 300):
            value = (i-center_x)**2 + (j-center_y)**2
            if value < 9:
                fftshift_fft_grid[i][j] = 0

    fft_gray = np.fft.fftshift(fftshift_fft_grid)

    final_image = abs(np.fft.ifft2(fft_gray))

    cv2.imwrite('processed_images/double_frequency_sinusoidal.png', final_image)

if __name__ == '__main__':
    do()