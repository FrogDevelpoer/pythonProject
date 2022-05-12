from keras.applications.vgg16 import VGG16

model = VGG16()
# print('type(model) : ', type(model))
# print('-' * 30)
#
# model.summary()
# print('-' * 30)

# VGG16 모델의 입력 이미지 크기 : 224, 224
target_width, target_height = 224, 224

img_source = '../image/'    # 이미지 출처
img_destination = '../myimage/'     # 파일을 저자할 경로

mylist = ['cat.jpg', 'fox.jpg', 'mydog.png', 'myrabbit.jpg']

from keras.preprocessing.image import load_img, img_to_array, array_to_img
from keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# total_data : 예측을 수행하기 위하여 전처리된 이미지 목록
total_data = []

for imgname in mylist:
    img = load_img(img_source + imgname, target_size=(target_width, target_height))
    plt.imshow(img)

    filename = img_destination + ' 사전 학습 모델 ' + imgname
    plt.savefig(filename)

    img_arr = img_to_array(img)
    # print(img_arr)

    pre_input = preprocess_input(img_arr)
    # print('pre_input.shape : ', pre_input.shape)
    total_data.append(pre_input)
# end for

import numpy as np
arr_input = np.stack(total_data)
print(arr_input.shape)

H = model.predict(arr_input)
# print('H OF SHAPE: ', H.shape)
# print('-' * 30)
#
# print('예측 값 표시')
# print(H)
# print('-' * 30)

from keras.applications.vgg16 import decode_predictions
result = decode_predictions(H, top=10)
# print(result)
# print('-' * 30)

totallist = []  # for csv file

for idx in range(len(mylist)):
    for bbb in range(len(result[idx])):
        sublist = [mylist[idx], result[idx][bbb][1], result[idx][bbb][2]]
        totallist.append(sublist)
    # inner for end
# outer for end

from pandas import DataFrame
mycolumn = ['image', 'description', 'probability']
myframe = DataFrame(totallist, columns=mycolumn)
filename = 'pretrainedResult.csv'
myframe.to_csv(filename, encoding='UTF-8')

# make bar chart
mycolor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#CCFFFF', '#CCFFDD', '#FFDDEE']
from pandas import Series

for idx in range(len(result)):  # 그림 개수 만큼
    plt.figure(figsize=(10, 8))

    data = []   # 그리고자 하는 확률 데이터
    captions = []   # x축에 놓일 caption

    for item in result[idx]:
        captions.append(item[1])
        data.append(item[2] * 100.0)
    # inner for end

    chartdata = Series(data, index=captions)
    chartdata.plot(kind='bar', rot=12, color=mycolor)
    plt.title('이미지 ' + mylist[idx] + ' 분류 결과')
    plt.ylim(-10, 100)
    plt.grid(True)

    filename = img_destination + mylist[idx].split('.')[0] + '.png'
    plt.savefig(filename)
    print(filename + ' 저장 완료')

# outer for end


print('fin')