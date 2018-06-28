import cv2
import numpy as np


def do():
    image = cv2.imread('raw_images/dog.png')

    height, width, channels = image.shape

    for k in range(0, channels):
        for i in range(0, height):
            for j in range(0, width):
                if 150 <= image[i][j][k] <= 200:
                    image[i][j][k] = 255

    cv2.imwrite('processed_images/sliced_dog.png', image)


if __name__ == '__main__':
    do()