import cmath
import cv2
import numpy as np


def do():
    blank_image = np.zeros((1000, 1000), np.complex)

    z = 0.5
    _lambda = 0.0000006328
    for i in range(0, 1000):
        for k in range(0, 1000):
            blank_image[i][k] = complex(0, 1) * complex(1.5 * 337.5) * complex((i-149)**2+(k-149)**2) * cmath.exp(complex(0, 1) * complex((i-149)**2 + (k-149)**2, 0)/complex(_lambda*z, 0)) / complex(_lambda*z, 0)

    max = 0.0
    min = 0.0
    for i in range(0, 1000):
        for j in range(0, 1000):
            value = abs(blank_image[i][j])
            if max < value:
                max = value

            if min > value:
                min = value
    print max,min
    blank_image = np.abs(blank_image)

    blank_image = blank_image * 255/max

    cv2.imwrite('processed_images/fresnel.png', blank_image)

    n = 1001
    I = np.arange(1, n)
    x = I - n / 2
    y = n / 2 - I

    R = 10

    X = x[:, np.newaxis]
    Y = y[np.newaxis, :]

    M = X ** 2 + Y ** 2 < R ** 2

    D1 = np.fft.fft2(M)

    fft_blank_image = np.fft.fft2(blank_image)

    ans = np.multiply(D1, fft_blank_image)

    ans = np.fft.ifft2(ans)

    cv2.imwrite('processed_images/circular_fresnel.png', np.abs(ans))


if __name__ == '__main__':
    do()