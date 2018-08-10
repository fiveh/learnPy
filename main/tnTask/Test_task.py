import math as mt
import os
import time

import cv2
import numpy as np

out_size = 16
path = 'C:/Users/hunter/Downloads/1k/'

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

    # print(arr)

    out = ''
    for i in arr:
        for j in range(len(arr) // 8):
            # print(i[8*j: 8*j+8: 1])

            zero_one = map(int, i[8 * j: 8 * j + 8: 1])  # convert True to 1, False to 0  using `int`
            # print(zero_one)
            n = int(''.join(map(str, zero_one)), 2)  # numbers to strings, join them
            # convert to number (base 2)
            out += ('{:02x}'.format(n))  # format them as hex string using `str.format`

    return out


def convert_to_hex_v2(img):
    diff = img[:, 1:] > img[:, :-1]

    hex_result = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    hex_result = '{:02x}'.format(hex_result)

    return hex_result


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
    global i
    message = 'NO FIND'
    count_mathces = 0

    count_in_collection = len(collection)
    size_image = len(image[0])

    for i in range(count_in_collection):
        if (len(collection[i]) == size_image):

            count_diff = 0
            for j in range(size_image):
                # if (i >= 4998):
                #     print(image[0], '\t', collection[i])
                if (image[0][j] != collection[i][j]):
                    count_diff += 1

            acc = (100 / len(image[0])) * count_diff
            if (acc < 15):
                message = 'Yes'
                print('difference: ', acc, '%')
                print('find on iteration', i, image)

    print(message, count_mathces, 'on: ', i)


def gen_collection(path, out_size):
    myhashes = []

    array_images = os.listdir(path)
    for image in array_images:
        img = cv2.imread(path + image)

        # hash = imagehash.average_hash(Image.open(path + image))
        # myhashes.append(hash)
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

        # bin_matrix = convert_to_bin(th1)

        result = convert_to_hex(bin_matrix)

        result2 = convert_to_hex_v2(result_dct)
        # print(result,'\n-----------')
        # print(result2)

        # myhashes.append(result)
        myhashes.append(result2)

        # print('itog \t -->', result)

        # show_image(image, th1)
        # save_image(path_to_save, image, th1)

    return myhashes


if __name__ == '__main__':
    all_files = gen_collection(path, out_size)
    one_file = gen_collection(path_one, out_size)

    start_time = time.time()

    hemming_length(one_file, all_files)

    print("Potracheno time: {:.3f} sec".format(time.time() - start_time))
