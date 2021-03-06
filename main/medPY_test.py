import os

import SimpleITK as sitk
import cv2
import matplotlib.pyplot as plt
import numpy as np

CONST_FROM = 90
CONST_TO = 100


# showing with cs2
def showing_gif(path):
    img = sitk.ReadImage(path)
    # print(img)

    for i in range(CONST_FROM, CONST_TO):
        # print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        cv2.imshow("tile", np.uint8(nptile))
        cv2.waitKey(5)


# showing with plt.show with uint8
def showing_gif_plt1(path):
    img = sitk.ReadImage(path)
    # for i in range(0, 155):

    for i in range(CONST_FROM, CONST_TO):
        # print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        plt.imshow(np.uint8(nptile))
        plt.show()
    # plt.close('all')
    plt.clf()
    plt.cla()
    # plt.re


# save images  to folder
def save_image(path, name_for_file):
    # print('path: \t', path)
    folder = 'hggs/'

    if (path.find('LGG') != -1):
        folder = 'lggs/'

    img = sitk.ReadImage(path)

    for i in range(CONST_FROM, CONST_TO):
        # print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        filename = name_for_file + str(i) + ".jpg"  # save all files
        # filename = str(i) + ".jpg"  # reWrite files
        path_to_folder = "../data/med_images/output_image/" + folder + filename
        # plt.imsave(path_to_folder, nptile, cmap=plt.cm.gray)  # for gray image save
        plt.imsave(path_to_folder, nptile)


# open All files in each folder
def open_all_files(path):  # open files to Folder BRATS2015
    count_files = 0
    yes_count = 0

    for first_lvl in os.listdir(path):
        print("1)", first_lvl)

        for second_lvl in os.listdir(path + first_lvl):
            print("\t2)", second_lvl)

            for third_lvl in os.listdir(path + first_lvl + "/" + second_lvl):
                path_to_file = path + first_lvl + "/" + second_lvl + "/" + third_lvl
                print("\t\t3)", third_lvl)

                if (path_to_file.find('more.XX') != -1 &
                        path_to_file.find('.OT.') != -1):
                    yes_count += 1

                # save_image(path_to_file, third_lvl)

                # showing_gif(path_to_file)
                # showing_gif_plt1(path_to_file)
                count_files += 1

    print("count files: ", count_files)  # all count files
    print("count more.XX files: ", yes_count)  # all count files

def rename_all_files(path_to_folder, name):
    count_files = 0
    for file in os.listdir(path_to_folder):
        print("---: ", file)
        old_name = path_to_folder + '/' + file
        new_name = path_to_folder + '/' + name + '.' + str(count_files) + '.jpg'
        os.rename(old_name, new_name)


        count_files += 1

    print("count files in folder: ", count_files)




if __name__ == "__main__":
    # path_training = "../data/med_images/input_image/BRATS2015/training/"  # ../BRATS2015/training/
    # open_all_files(path_training)

    # path0 = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain_3more.XX.O.OT.54517.mha"

    # Flair = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain.XX.O.MR_Flair.54512.mha"
    # T1 = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain.XX.O.MR_T1.54513.mha"
    # T1c = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain.XX.O.MR_T1c.54514.mha"
    # T2 = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain.XX.O.MR_T2.54515.mha"
    # OT = "../data/med_images/input_image/BRATS2015/training/HGG/brats_2013_pat0001_1/VSD.Brain_3more.XX.O.OT.54517.mha"


    #
    # showing_gif(path0)
    # save_image(path0, "name1")
    # showing_gif_plt1(path1)
    #
    # save_image(Flair, "name1")
    # save_image(T1, "name2")
    # save_image(T1c, "name3")
    # save_image(T2, "name4")
    # save_image(OT, "name5")

    open_all_files("../data/med_images/input_image/BRATS2015/training/")


    # rename_all_files("../data/med_images/output_image/hggs", 'hgg')
    # rename_all_files("../data/med_images/output_image/lggs", 'lgg')
