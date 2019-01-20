import os
import shutil

with open('cooldrink_test.txt', 'r') as f:
	for line in f:
		filename = line.rstrip().split('data/')[-1]
		shutil.copy(filename, 'input/test/')
		shutil.copy(filename.split('.')[0]+'.xml', 'input/test/')
		# break

with open('cooldrink_train.txt', 'r') as f:
	for line in f:
		filename = line.rstrip().split('data/')[-1]
		shutil.copy(filename, 'input/train/')
		shutil.copy(filename.split('.')[0]+'.xml', 'input/train/')