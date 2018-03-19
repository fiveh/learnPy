import SimpleITK as sitk
import numpy as np
import cv2


path = '../data/med_images/VSD.Brain.XX.O.MR_Flair.54193.mha'
path1 = '../data/med_images/VSD.Brain.XX.O.MR_T1.54194.mha'
path2 = '../data/med_images/VSD.Brain.XX.O.MR_T1c.54195.mha'
path3 = '../data/med_images/VSD.Brain.XX.O.MR_T2.54196.mha'

def showingGif(path):
    img = sitk.ReadImage(path)
    for i in range(0, 155):
        print("frame ", i)
        tile = sitk.Tile(img[:, :, i])
        nptile = sitk.GetArrayFromImage(tile)
        if (i == 95):
            cv2.waitKey(1000)
        cv2.imshow("tile", np.uint8(nptile))
        cv2.waitKey(10)



showingGif(path)
showingGif(path1)
showingGif(path2)
showingGif(path3)