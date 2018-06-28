from collections import defaultdict

import numpy as np
import cv2


def do():
    image = cv2.imread('raw_images/dog.png')
    height, width, channels = image.shape
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    intensity_to_probability_map = defaultdict(dict)

    for k in range(0, channels):
        for i in range(0, height):
            for j in range(0, width):
                if image[i][j][k] not in intensity_to_probability_map[k]:
                    intensity_to_probability_map[k][image[i][j][k]] = 0
                else:
                    intensity_to_probability_map[k][image[i][j][k]] += 1


    for k in range(0, channels):
        for intensity, number in intensity_to_probability_map[k].iteritems():
            intensity_to_probability_map[k][intensity] = float(number)/(height * width)

    for k in range(0, channels):
        values = intensity_to_probability_map[k].keys()
        values.sort()

        previous = 0.0
        for i in values:
            intensity_to_probability_map[k][i] += previous
            previous = intensity_to_probability_map[k][i]


        for i in range(0, height):
            for j in range(0, width):
                image[i][j][k] = 255*intensity_to_probability_map[k][image[i][j][k]]


    cv2.imwrite('processed_images/contrast_stretched_image.jpg', image)


if __name__=='__main__':

    do()