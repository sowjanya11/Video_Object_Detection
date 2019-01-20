import cv2
import os
import csv
import numpy as np

if __name__ == '__main__':
    # root_folder = "training images/"
    training_data_file = 'cooldrink_test.txt'
    classes = {"appy": 0, "fanta": 1, "appyfizz": 2, "sprite": 3}
    winname= "Create Bounding box"

    with open(training_data_file, 'r') as f:
        for line in f:
            print(line)
            temp_text = line.rstrip().split(" ")
            object_id = classes[temp_text[-1]]
            img_path = " ".join(temp_text[0:-1])
            img_filename_ext = img_path.split("/").pop()
            img_filename =img_filename_ext.split('.')[0]

            # print(object_id, img_filename)
            img = cv2.imread(img_path)

            clone = img.copy()
            r = cv2.selectROI(winname, img)
            temp_rect = np.array([r[0], r[1], r[0] + r[2], r[1] + r[3]])
            cv2.rectangle(clone, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), (0,255,0), 1)

            W = img.shape[1]
            H = img.shape[0]
            w = float(r[2])/W
            h = float(r[3])/H
            center_x = float(r[0])/W
            center_y = float(r[1])/H

            cv2.imshow(winname, clone)
            with open('labels/' + img_filename +'.txt', 'w') as outfile:
                    fieldnames = ['object_class_id', 'center-x', 'center-y', 'width', 'height']
            #         # print(fieldnames)
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=" ")

            #         # writer.writeheader()
                    writer.writerow({'object_class_id': object_id,
                                     'center-x': center_x,
                                     'center-y': center_y,
                                     'width': w,
                                     'height': h
                                    })

            k = cv2.waitKey(0)
            # print(field_obj)

            if k == 'ESC':
                exit(0)
            if k == 'ENTER':
                continue

            # break
