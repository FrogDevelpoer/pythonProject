# 원본 이미지가 있는 폴더
origin_data_folder = '../datasets/cats_and_dogs'

# 학습, 검증, 테슽트를 위한 개별 폴더 생성
target_folder = '../datasets/cats_and_dogs_random'

import os
import shutil    # shell utility

if os.path.exists(target_folder):
    shutil.rmtree(target_folder)

os.mkdir(target_folder)

upp_folder = ['cat', 'dog']
low_folder = ['train', 'validation', 'test']
data_size = [0, 1000, 1500, 2000]

for low in low_folder:
    subfolder = os.path.join(target_folder, low)
    os.mkdir(subfolder)
    for upp in upp_folder:
        somfolder = os.path.join(subfolder, upp + 's')
        os.mkdir(somfolder)

import numpy as np

for upp in upp_folder:
    mylist = [upp + '.' + str(i) + '.jpg' for i in range(2000)]
    # print(mylist)
    newdata = np.random.permutation(mylist)

    idx = 0
    for low in low_folder:
        filelist = newdata[data_size[idx]:data_size[idx + 1]]

        idx += 1
        for fname in filelist:
            src = os.path.join(origin_data_folder, fname)
            newtarget = target_folder + '/' + low + '/' + upp + 's'
            dst = os.path.join(newtarget, fname)
            shutil.copyfile(src, dst)

print('fin')