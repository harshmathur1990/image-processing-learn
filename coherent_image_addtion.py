import cv2
import math
import numpy as np
import scipy
import scipy.signal


def do():
    image = cv2.imread('raw_images/image_addition.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    grid = np.zeros((300, 300), np.float)

    for y in range(0, 300):
        for x in range(0, 300):
            grid[x][y] = (1 + math.cos(2 * np.pi * y * 10 / 101)) * 255

    fft_grid = np.fft.fft2(grid)
    fft_shift_grid = np.fft.fftshift(fft_grid)
    convolution = scipy.signal.convolve2d(gray_image, fft_shift_grid)
    cv2.imwrite('coherent_image_addition.png', np.abs(convolution))


if __name__ == '__main__':
    do()