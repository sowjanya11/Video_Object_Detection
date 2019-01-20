import cv2

im = cv2.imread('fg1.jpg')
# (x,y,w,h) = cv2.selectROI(im)
w = im.shape[1]
h = im.shape[0]
k = 64
steps_x = int(w/k)
steps_y = int(h/k)
print(steps_x, steps_y)

# for i in range(steps_x-1):
for j in range(steps_x):
	img = im[64:,j*k:(j+2)*k]

	ratio = 200/img.shape[0]
	cropped_im = cv2.resize(img, (0,0), fx=ratio, fy=ratio)
	# cv2.imshow('img', img)
	# cv2.waitKey(0)
	cv2.imwrite('fg' + '_' + str(j) + '.png', cropped_im)