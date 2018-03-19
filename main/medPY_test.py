# TODO: try to run data on Keras CNN
# TODO: take the more important data from 155 set

import SimpleITK as sitk
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


# showing with cs2
def showingGif(path):
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


# FIXME:  fix size of 'for' function
# showing with plt.show with uint8
def showingGifPlt1(path):
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


# save images  to folder
def saveImage(path):
    img = sitk.ReadImage(path)
    for i in range(0, 155):
        print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        # plt.imshow(nptile)
        # plt.show()
        filename = str(i)+".jpg"
        path_to_folder = "../data/med_images/output_image/"+filename
        plt.imsave(path_to_folder, nptile)


# open All files in each folder
def openAllFiles():
    for filename in os.listdir("D:/BRATS2015/training/HGG"):
        for filenamein in os.listdir("D:/BRATS2015/training/HGG/"+filename):
            print(filenamein)
            showingGif("D:/BRATS2015/training/HGG/"+filename+"/"+filenamein)



path0 = '../data/med_images/VSD.Brain.XX.O.MR_Flair.54193.mha'
path1 = '../data/med_images/VSD.Brain.XX.O.MR_T1.54194.mha'
path2 = '../data/med_images/VSD.Brain.XX.O.MR_T1c.54195.mha'
path3 = '../data/med_images/VSD.Brain.XX.O.MR_T2.54196.mha'


# saveImage(path0)
# saveImage(path1)
# saveImage(path2)