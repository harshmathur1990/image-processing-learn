import cv2
import numpy as np


def do():
    image = cv2.imread('raw_images/dog.png')
    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    fft_gray = np.fft.fft2(gray_image)
    fft_shift_gray_image = np.fft.fftshift(fft_gray)

    center_x, center_y = height/2, width/2

    for i in range(0, height):
        for j in range(0, width):
            value = (i-center_x)**2 + (j-center_y)**2
            if value > 100:
                fft_shift_gray_image[i][j] = 0

    fft_gray = np.fft.fftshift(fft_shift_gray_image)

    final_image = abs(np.fft.ifft2(fft_gray))

    cv2.imwrite('processed_images/low_pass_dog.png', final_image)


if __name__ == '__main__':
    do()