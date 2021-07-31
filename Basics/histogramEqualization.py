import numpy as np
import matplotlib.pyplot as plt
import cv2


def cumulative_sum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)


def get_graynum(image, bins):
    num = np.zeros(bins)
    for pixel in image:
        num[pixel] += 1
    return num


def histogramEqualization(inimg):
    gray = cv2.imread(inimg, 0)

    gray_flat = gray.flatten()
    num = get_graynum(gray_flat, 256)

    CS = cumulative_sum(num)

    numerator = (CS - CS.min()) * 255
    N = CS.max() - CS.min()

    CS = numerator / N

    new = CS[gray_flat]
    new = np.reshape(new, gray.shape)

    plt.imshow(new, cmap='gray')

    plt.show()


