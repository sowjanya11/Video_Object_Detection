import cv2
import os
import imutils
import numpy as np


def decreaseBrightness(im, root, index):
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # h, s, v = cv2.split(hsv)

    # lim = 255 - value
    hsv[:,:,2] = hsv[:,:,2]*0.4
    # v[v > lim] = 0
    # v[v <= lim] += value

    # final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    return img
    # cv2.imwrite(root + 'appy_fizz1_'+ str(index) + '.jpg', img)

def rotateImages(im, root, index):
    # loop over the rotation angles
    # for angle in np.arange(0, 360, 15):
    #     rotated = imutils.rotate(im, angle)
    #     cv2.imshow("Rotated (Problematic)", rotated)
    #     cv2.waitKey(0)
    i = 0
    # loop over the rotation angles again, this time ensuring
    # no part of the image is cut off
    for angle in np.arange(0, 360, 90):
        rotated = imutils.rotate_bound(im, angle)
        # cv2.imshow("Rotated (Correct)", rotated)
        # cv2.waitKey(0)
        cv2.imwrite(root + "appyfizz1_" + str(index) + '_' + str(i) + '.jpg', rotated)
        i += 1



if __name__ == '__main__':
    root = 'training_images/appyfizz/'

    files = os.listdir(root)

    count = len(files)

    for i,file in enumerate(files):
        print(file)
        filename = root + file

        im = cv2.imread(filename)
        # im = decreaseBrightness(im, root, i)
        rotateImages(im, root, i)
        break
        # kernel = np.ones((7,7),np.float32)/49
        # im = cv2.filter2D(im,-1,kernel)

        # cv2.imshow('image', im)
        # cv2.waitKey(0)
        # cv2.imwrite(root + "sprite2_" + str(i) + '.jpg', im)
        # break

