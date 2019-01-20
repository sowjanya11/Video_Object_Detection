import numpy as np
import cv2 as cv
# from matplotlib import pyplot as plt
img = cv.imread('edited_thumbnails/img054.png')
mask = 3*np.ones(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

mask[0:100,0:200] = 0
# mask[:,0:20] = 0
mask[0:50, :] = 0
mask[:, img.shape[1]-20:img.shape[1]] = 0
# mask = np.zeros(img.shape[:2],np.uint8)
# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)
# rect = (50,50,450,290)
mask, bgdModel, fgdModel = cv.grabCut(img,mask,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# mask2 = np.where((mask==0).astype('uint8')
img = img*mask2[:,:,np.newaxis]

mask = 3*np.ones(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
mask[:,0:20] = 0
mask, bgdModel, fgdModel = cv.grabCut(img,mask,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# mask2 = np.where((mask==0).astype('uint8')
img = img*mask2[:,:,np.newaxis]

mask = 3*np.ones(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
mask[img.shape[0]-10:img.shape[0],0:50] = 0
mask, bgdModel, fgdModel = cv.grabCut(img,mask,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# mask2 = np.where((mask==0).astype('uint8')
img = img*mask2[:,:,np.newaxis]


# for y in range(img.shape[0]):
# 	for x in range(img.shape[1]):
# 		if img[y,x,:].all() == 0:
# 			img[y,x,:] = 255

# plt.imshow(img),plt.colorbar(),plt.show()
# cv.imshow('img', img)
# cv.waitKey(0)
cv.imwrite('fg1.jpg', img)