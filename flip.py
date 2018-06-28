import cv2
import numpy as np


def get_flip_image(image_path, flip_image_path):
    image = cv2.imread(image_path)
    width, height, channels = image.shape
    flipped_image = np.zeros((width, height,3), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            flipped_image[width - j - 1][height - i - 1][0] = image[j][i][0]
            flipped_image[width - j - 1][height - i - 1][1] = image[j][i][1]
            flipped_image[width - j - 1][height - i - 1][2] = image[j][i][2]
    cv2.imwrite(flip_image_path, flipped_image)


if __name__ == "__main__":
    image_path = 'raw_images/dog.png'
    flip_image_path = 'processed_images/dog_flipped.jpg'
    get_flip_image(image_path, flip_image_path)