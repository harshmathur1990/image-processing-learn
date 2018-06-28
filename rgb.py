import cv2
import numpy as np
import copy


def block_channels(image, k):
    img = copy.deepcopy(image)
    height, width, channels = img.shape
    for l in range(0, channels):
        if k == l:
            continue
        for i in range(0, height):
            for j in range(0, width):
                img[i][j][k] = 0.0
    return img


def do():
    image = cv2.imread('raw_images/dog.png')
    red = block_channels(image, 0)
    green = block_channels(image, 1)
    blue = block_channels(image, 2)
    cv2.imwrite('processed_images/red_dog.png', red)
    cv2.imwrite('processed_images/green_dog.png', green)
    cv2.imwrite('processed_images/blue_dog.png', blue)


if __name__ == '__main__':
    do()