import cv2
import numpy as np


def do():
    image = cv2.imread('raw_images/dog.png')
    height, width, channels = image.shape

    for k in range(0, channels):
        for i in range(0, height):
            for j in range(0,width):
                image[i][j][k] = 255 - image[i][j][k]

    cv2.imwrite('processed_images/negative_dog.png', image)


if __name__ == '__main__':
    do()