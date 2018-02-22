import cv2
import numpy as np


def get_binary_image(image_path, gray_image_path, binary_image_path):
    image = cv2.imread(image_path)
    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary_image = np.zeros((height,width,1), np.uint8)
    cv2.imwrite(gray_image_path, gray_image)
    for i in range(0, height):
        for j in range(0,width):
            binary_image[i][j] = 0 if gray_image[i][j] <= 100 else 255
    cv2.imwrite(binary_image_path, binary_image)
    cv2.imshow('binary_image',binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = 'raw_images/2.jpg'
    gray_image_path = 'processed_images/2_gray.jpg'
    binary_image_path = 'processed_images/2_binary.jpg'
    get_binary_image(image_path, gray_image_path, binary_image_path)