import random
import os
import subprocess
import sys

def split_data_set(image_dir, label):
    f_val = open("cooldrink_test.txt", 'a')
    f_train = open("cooldrink_train.txt", 'a')
    
    files = os.listdir(image_dir)
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    
    for f in os.listdir(image_dir):
        if(f.split(".")[1] == "jpg"):
            ind += 1
            
            if ind in test_array:
                f_val.write(image_dir+'/'+f+' '+ label +'\n')
            else:
                f_train.write(image_dir+'/'+f+' '+ label +'\n')

classes = ['appy', 'appyfizz', 'fanta', 'sprite']
for cl in classes:
    split_data_set('training images/' + cl, cl)
