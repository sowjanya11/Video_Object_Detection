import cv2
import os
import csv

def modifyvalues(x, modified_width, modified_height):
    X = [x[0], int(x[1]*modified_width), int(x[2]*modified_height), int(x[3]*modified_width), int(x[4]*modified_height)]

    # cv2.rectangle(im,(X[1] - 100, X[2]), (X[1] - 100 + X[3], X[2] + X[4]), (0,255,0), 1)
    # cv2.imshow('img', im)
    # cv2.waitKey(0)
    modified_values = [X[0], X[1]/160, X[2]/96, X[3]/160, X[4]/96]
    return modified_values


if __name__ == '__main__':
    # root = 'training images copy/appyfizz/'
    # files = os.listdir(root)

    # if '.DS_Store' in files:
    #   files.remove('.DS_Store')

    # for img_file in files:
    #   img = cv2.imread(root + img_file)
    #   height = img.shape[0]
    #   ratio = 96/height
    #   img = cv2.resize(img, (0,0), fx=ratio, fy=ratio)
    #   print(img.shape)

    #   with open('labels old/' + img_file.split('.')[0] + '.txt', 'r') as f:
    #     val_arr = f.read().rstrip().split(' ')
    #     val_arr = [int(val_arr[0])] + [float(x) for x in val_arr[1:]]
    #   # # x = [0, 0.27, 0.26222222222222225, 0.5075, 0.5822222222222222]
    #   x = val_arr
    #   # # print(img[:, 100:400].shape)
    #   X = [0, int(x[1]*171), int(x[2]*96), int(x[3]*171), int(x[4]*96)]
    #   # print(X)
    #   cropped_im = img[:, 0:160]
    #   # cropped_im = img
    #   print(cropped_im.shape)

    #   # cv2.rectangle(cropped_im, (X[1],X[2]), (X[3]+X[1], X[2]+X[4]), (0,0,0), 1)

    #   # cv2.imshow('img', cropped_im)
    #   # cv2.waitKey(0)
    #   # break
    #   cv2.imwrite('training-images-96/appyfizz/' + img_file, cropped_im)
    root = 'labels old/'
    files = os.listdir(root)

    for txt_file in files:
        with open(root + txt_file, 'r') as f:
            val_arr = f.read().rstrip().split(' ')
            val_arr = [int(val_arr[0])] + [float(x) for x in val_arr[1:]]

            print(val_arr)
            # if 'appy_fizz' in txt_file:
            #     modified_width = 534
            # elif 'appy' in txt_file:
            #     modified_width = 533
            # else:
            #     modified_width = 534

            # print(modified_width)
            # im = cv2.imread("training images/appy/appy1_60.jpg")
            finalvals = modifyvalues(val_arr, 160, 96)
            print(finalvals)
            with open('labels_96/' + txt_file, 'w') as outfile:
                fieldnames = ['object_class_id', 'center-x', 'center-y', 'width', 'height']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=" ")
                writer.writerow({'object_class_id': finalvals[0],
                                 'center-x': finalvals[1],
                                 'center-y': finalvals[2],
                                 'width': finalvals[3],
                                 'height': finalvals[4]
                                })

        # break


