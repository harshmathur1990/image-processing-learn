import cv2
import numpy as np
from matplotlib import pyplot as plt
import pylab as py


def do():
    image1 = cv2.imread('raw_images/dog.png')
    gray_image_1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.imread('processed_images/circular_fraunhaufer.png')
    gray_image_2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    image_3 = gray_image_1 + gray_image_2

    cv2.imwrite('processed_images/addition.png', image_3)


if __name__ == '__main__':
    do()

