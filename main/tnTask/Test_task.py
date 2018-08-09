import math as mt
import os

import cv2
import imagehash
from PIL import Image
import numpy as np
import time

out_size = 16
path = 'C:/Users/hunter/Downloads/st/'

path_one = 'C:/Users/hunter/Downloads/search/'
path_to_save = 'C:/Users/hunter/Downloads/saving/'


def show_image(name, image):
    """
    show image
    :param name: will show on title
    :param image: image
    """
    cv2.imshow(name, image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()

def save_image(path_to_save, name, image):
    cv2.imwrite(path_to_save + 'new.' + name, image)  # saving image to current

def convert_to_bin(arr):
    for i in range(out_size):
        for j in range(out_size):
            if (arr[i][j] > 0):
                arr[i][j] = True
            else:
                arr[i][j] = False
    return arr

def convert_to_hex(arr):  # input bin array
    out = ''
    for l in arr:
        zero_one = map(int, l)  # convert True to 1, False to 0  using `int`
        n = int(''.join(map(str, zero_one)), 2)  # numbers to strings, join them
        # convert to number (base 2)
        out += ('{:02x}'.format(n))  # format them as hex string using `str.format`

    return out

def dct(out_size):
    arr = []

    for i in range(out_size):
        sum = 0
        arr.append([])
        for j in range(out_size):
            sum += mt.cos((2 * j + 1) * i * mt.pi / (2 * out_size))
            arr[i].append(mt.sqrt(2 / out_size) * sum)

    return (arr)

def hemming_length(image, collection):
    # print(collection)
    message = 'NO FIND'

    size_image = len(image[0])
    size_image_in_col = len(collection[0])
    count_in_collection = len(collection)

    print('im', size_image)
    print('i in col ', size_image_in_col)
    print('collection', count_in_collection)

    print(image[0])
    print(collection[0])

    for i in range(count_in_collection):
        count_diff = 0
        for j in range(size_image):
            if (image[0][j] != collection[i][j]):
                count_diff += 1

        acc = (100/len(image[0]))*count_diff
        if (acc < 30):
            message = 'Yes'
            print('difference: ', acc, '%')
            print(image,'find on iteration', i)
    print(message)

def gen_collection(path, out_size):
    myhashes = []

    array_images = os.listdir(path)
    for image in array_images:
        img = cv2.imread(path + image)

        # hash = imagehash.average_hash(Image.open(path + image))
        # hashes.append(hash)
        # print('phash \t -->', hash)

        # resize all images to SIZE
        img = cv2.resize(img, (out_size, out_size))

        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        avg = cv2.mean(img)

        ret, th1 = cv2.threshold(img, avg[0], 255, cv2.THRESH_BINARY)

        dct_matrix = dct(out_size)
        dct_t_matrix = np.transpose(dct_matrix)
        result_dct = dct_matrix * th1 * dct_t_matrix
        bin_matrix = convert_to_bin(result_dct)

        # print(len(bin_matrix), '\t', image)


        # bin_matrix = convert_to_bin(th1)

        result = convert_to_hex(bin_matrix)

        print(len(result), '\t', image)

        myhashes.append(result)

        # print('itog \t -->', result)

        # show_image(image, th1)
        # save_image(path_to_save, image, th1)

    return myhashes


if __name__ == '__main__':

    all_files = gen_collection(path, out_size)
    one_file = gen_collection(path_one, out_size)

    start = time.time()

    hemming_length(one_file, all_files)


    print("Potracheno time: {:.3f} sec".format(time.time()-start))

