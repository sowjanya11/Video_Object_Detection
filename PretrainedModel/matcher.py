##This file is not used. This is just to check how many matches found using ORB method

import numpy as np
import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



# img1 = cv2.imread('cropped_im6.png',0)          # queryImage
# img2 = cv2.imread('training_images/fanta/fanta0.jpg',0) # trainImage
# # Initiate ORB detector
ORB = cv2.ORB_create()
# # find the keypoints and descriptors with ORB
# kp1, des1 = orb.detectAndCompute(img1,None)
# kp2, des2 = orb.detectAndCompute(img2,None)

# # create BFMatcher object
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# # Match descriptors.
# matches = bf.match(des1,des2)
# # Sort them in the order of their distance.
# matches = sorted(matches, key = lambda x:x.distance)
# print(matches, len(matches))
# # Draw first 10 matches.
# img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)
# plt.imshow(img3),plt.show()


temp1 = cv2.imread('fg.jpg')
temp2 = cv2.imread('cooldrinks/fanta/fanta0.jpg')
kp1 = None
kp2 = None
des1 = None
des2 = None
thresh_norm = temp1.shape[1]/160

if temp1 is not None and temp2 is not None:
    #ORB keypoints and descriptors
    kp1, des1 = ORB.detectAndCompute(temp1, None)
    kp2, des2 = ORB.detectAndCompute(temp2, None)

    if len(kp1) >= 2 and len(kp2) >= 2:
        keypoints_check = True
    else:
        keypoints_check = False

    if des1 is not None and des2 is not None and keypoints_check:
        # Flann Matching
        FLANN_INDEX_LSH = 6
        index_params = dict(algorithm=FLANN_INDEX_LSH,
                            table_number=6,  # 12
                            key_size=12,  # 20
                            multi_probe_level=2)  # 2
        search_params = dict(checks=50)  # or pass empty dictionary

        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(np.asarray(des1), np.asarray(des2), k=2)
        # Apply ratio test
        matchesMask = [[0, 0] for i in range(len(matches))]
        count = 0
        # # ratio test as per Lowe's paper
        for i, item in enumerate(matches):
            # if len(item) == 2:
            #     (m, n) = item
            #     if m.distance < 0.7 * n.distance:
            #         matchesMask[i] = [1, 0]
            count = count + 1

        print(count)