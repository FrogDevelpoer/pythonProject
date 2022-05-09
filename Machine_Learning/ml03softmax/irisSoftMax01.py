import numpy as np
filename = 'iris.csv'

import pandas as pd
df = pd.read_csv(filename)
print(df.head())

label = 'Species'
print(df[label].unique())

import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df, hue=label)
filename = 'irisSoftMax01_01.png'
plt.savefig(filename)
print(filename + '파일 저장')

data = df.values

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y_raw = data[:, x_column:].ravel()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(y_raw)
y = le.transform(y_raw)

x = x.astype(float)
y = y.astype(float)

from sklearn.model_selection import train_test_split

seed = 1234
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=seed)

nb_classes = 3

from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train, num_classes=nb_classes, dtype='float32')

from tensorflow.python.keras.models import Sequential
model = Sequential()

from tensorflow.python.keras.layers import Dense
model.add(Dense(units=nb_classes, input_shape=(x_column,), activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=1000, verbose=0, validation_split=0.3)
print(history)

plt.rc('font', family='Malgun Gothic')
plt.figure()

plt.plot(history.history['loss'], 'b--', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')

plt.xlabel('epoch에 따른 손실 정보')
plt.legend()
filename = 'irisSoftMax01_02.png'
plt.savefig(filename)
print(filename + '저장 완료')

csvDataList = []
hit = 0.0

import numpy as np

for idx in range(len(x_test)):
    H = model.predict(np.array([x_test[idx]]))
    prediction = np.argmax(H, axis=-1)
    print('예측 값 : ', prediction, end='')
    print('정답 : [%d]' % int(y_test[idx]), end='')

    sublist = []
    sublist.append(prediction[0])
    sublist.append(int(y_test[idx]))

    _H = H.flatten()

    for idx2 in range(len(_H)):
        sublist.append(_H[idx2])
    csvDataList.append(sublist)

    hit += float(prediction[0] == int(y_test[idx]))

hitrate = 100 * hit / len(x_test)
print('정확도 : %.4f' % hitrate)

mycolumns=['예측값', '정답', '확률01', '확률02', '확률03']
df=pd.DataFrame(csvDataList, columns=mycolumns)
csvfilename='irisSoftMaxCsv.csv'
df.to_csv(csvfilename, index=False, encoding='cp949')
print(csvfilename + ' 파일이 저장됨')

print('finished')

