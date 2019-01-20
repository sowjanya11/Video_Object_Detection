import cv2
import os

if __name__ == '__main__':
	root = 'training_images/'
	classes = ['appy', 'fanta', 'appyfizz', 'sprite']

	txt_files = os.listdir('labels')

	if '.DS_Store' in txt_files:
		txt_files.remove('.DS_Store')

	for file in txt_files:
		filename = file.split('.')[0] + '.jpg'
		print(filename)
		

		with open('labels/'+file, 'r') as f:
			arr = f.read().rstrip().split(" ")

			class_id = int(arr[0])
			x = int(float(arr[1])*320)
			y = int(float(arr[2])*320)
			w = int(float(arr[3])*320)
			h = int(float(arr[4])*320)
			img = cv2.imread(root + str(classes[class_id]) + '/' + filename)

			cv2.imwrite('cooldrinks/' +str(classes[class_id])+'/'+filename, img[y:y+h,x:x+w])


		# break

