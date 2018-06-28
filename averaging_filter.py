import cv2
import numpy as np
import scipy
import scipy.signal

def do():
    image = cv2.imread('raw_images/dog.png')

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    w, h = 8, 5;
    averaging_filter = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, 5):
        for j in range(0, 5):
            averaging_filter[i][j] = float(1)/float(25)

    convolution = scipy.signal.convolve2d(gray_image, averaging_filter)

    cv2.imwrite('processed_images/average_dog.png', convolution)


if __name__ == '__main__':
    do()