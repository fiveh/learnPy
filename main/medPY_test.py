# TODO: try to run data on Keras CNN
# TODO: take the more important data from 155 set

import SimpleITK as sitk
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


# showing with cs2
def showing_gif(path):
    img = sitk.ReadImage(path)
    for i in range(0, 155):
        # print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        # print(nptile)
        # if (i == 95):
        #     cv2.waitKey(2000)
        cv2.imshow("tile", np.uint8(nptile))
        cv2.waitKey(10)


# FIXME:  fix size of 'for' function, because not all files is printing
# showing with plt.show with uint8
def showing_gif_plt1(path):
    img = sitk.ReadImage(path)
    # for i in range(0, 155):
    for i in range(90, 100):
        print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        plt.imshow(np.uint8(nptile))
        plt.show()
    # plt.close('all')
    plt.clf()
    plt.cla()
    # plt.re


# FIXME:  choose the main images from 0 to 155 frames
# save images  to folder
def save_image(path, name_for_file):
    img = sitk.ReadImage(path)
    # for i in range(0, 155):
    for i in range(85, 105):
        print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        # filename = str(i) + name_for_file + ".jpg"  # save all files
        filename = str(i) + ".jpg"  # reWrite files
        path_to_folder = "../data/med_images/output_image/" + filename
        plt.imsave(path_to_folder, nptile)


# open All files in each folder
def open_all_files(path):  # open files to Folder BRATS2015
    count_files = 0
    for first_lvl in os.listdir(path):
        print("1)", first_lvl)
        for second_lvl in os.listdir(path + first_lvl):
            print("\t2)", second_lvl)
            for third_lvl in os.listdir(path + first_lvl + "/" + second_lvl):
                path_to_file = path + first_lvl + "/" + second_lvl + "/" + third_lvl
                print("\t\t3)", third_lvl)
                save_image(path_to_file, third_lvl)
                # showing_gif(path_to_file)
                count_files += 1

    print("count files: ", count_files)  # all count files


if __name__ == "__main__":


    path_training = "../data/med_images/input_image/BRATS2015/training/"  # ../BRATS2015/training/
    open_all_files(path_training)

    # path0 = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain_3more.XX.O.OT.54517.mha"
    # path1 = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain.XX.O.MR_Flair.54512.mha"
    # showing_gif(path0)
    # save_image(path0)
    # showing_gif(path1)
    # save_image(path1)

