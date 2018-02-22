import cv2
import numpy as np


def get_amplified_image(image_path, amplified_image_path, factor=2):
    image = cv2.imread(image_path)
    height, width, channels = image.shape
    amplified_image = np.zeros((height,width,3), np.uint8)
    for i in range(0, height):
        for j in range(0,width):
            amplified_image[i][j][0] = min(factor * image[i][j][0], 255)
            amplified_image[i][j][1] = min(factor * image[i][j][1], 255)
            amplified_image[i][j][2] = min(factor * image[i][j][2], 255)
    cv2.imwrite(amplified_image_path, amplified_image)

if __name__ == "__main__":
    image_path = 'raw_images/2.jpg'
    amplified_image_path = 'processed_images/2_amplified.jpg'
    factor = 2
    get_amplified_image(image_path, amplified_image_path, factor)