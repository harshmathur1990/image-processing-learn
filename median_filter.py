import numpy as np
import cv2
import scipy
import scipy.signal


def add_salt_and_pepper(image):
    s_vs_p = 0.5
    amount = 0.004
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in image.shape]
    out[coords] = 0
    return out


def do():
    image = cv2.imread('raw_images/dog.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = add_salt_and_pepper(gray_image)

    cv2.imwrite('processed_images/dog_salt_pepper.png', image)

    convolution = scipy.signal.medfilt(image, kernel_size=5)

    cv2.imwrite('processed_images/median_dog.png', convolution)

if __name__ == '__main__':
    do()