import cv2
import os

if __name__ == '__main__':
    thumbnails = sorted(os.listdir('thumbnails1'))
    x = 105
    y = 70
    w = 230
    h = 125

    if '.DS_Store' in thumbnails:
        thumbnails.remove('.DS_Store')

    for i, file in enumerate(thumbnails):
        im = cv2.imread('thumbnails/' + file)
        # cv2.imshow('img', im)
        # cv2.waitKey(0)
        print(im.shape)

        # if i == 10:
        #     (x, y, w, h) = cv2.selectROI(im)
        #     print(x,y,w,h)
        #     break

        # edges = cv2.Canny(im, 100, 200)

        cropped_im = im[70:185,105:335]

        hsv = cv2.cvtColor(cropped_im, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        value = 70

        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        ratio = 300/img.shape[0]
        img = cv2.resize(img, (0,0), fx=ratio, fy=ratio)

        # cv2.imshow('image', img)
        # cv2.waitKey(0)
        cv2.imwrite("edited_thumbnails/" + file, img)