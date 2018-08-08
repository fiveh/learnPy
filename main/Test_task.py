import math as mt
import os
import numpy as np

import cv2

out_size = 8
path = 'C:/Users/hunter/Downloads/tests_data/st/'


def show_image(name, image):
    """
    show image
    :param name: will show on title
    :param image: image
    """
    cv2.imshow(name, image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()


def save_image(name, image):
    cv2.imwrite(path + 'new.' + name, image)  # saving image to current


array_images = os.listdir(path)
for image in array_images:
    img = cv2.imread(path + image)

    # resize all images to SIZE
    img = cv2.resize(img, (out_size, out_size))

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    avg = cv2.mean(img)

    ret, th1 = cv2.threshold(img, avg[0], 255, cv2.THRESH_BINARY)

    # show_image(image, th1)
    # save_image(image, th1)

    arr = []

    for i in range(out_size):
        sum = 0
        arr.append([])
        for j in range(out_size):
            sum += mt.cos((2*j+1)*i*mt.pi/(2*out_size))
            arr[i].append(mt.sqrt(2 / out_size) * sum)

        # print(sum)
            # print(th1[i][j])

        # print('\n')

    print(arr)


    # sp.fft(th1)

    # print(th1[0][0])

    # for i in range(out_size):
    #     print(th1[i])
    #
    # print('\n\n')

# print(path)


print('-------------------')


