filename = 'wine.csv'

import pandas as pd
df_wine = pd.read_csv(filename, header=None)

print('df_wine.shape : ', df_wine.shape)
print('-' * 30)

df = df_wine.sample(frac=0.15)  # 15%만 비복원 샘플링
print('df.shape : ', df.shape)
print('-' * 30)

data = df.values
table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
model = Sequential()

model.add(Dense(units=30, activation='relu', input_dim=x_column))
model.add(Dense(units=12, activation='relu'))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=y_column, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# ModelCheckPoint 콜백 함수가 생성해주는 파일을 저장하기 위한 폴더
model_dir = './model/'
import os
if not os.path.exists(model_dir):
    os.mkdir(model_dir)
model_name = model_dir + '{epoch:02d}-{val_loss:4f}.hdf5'

from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint

es = EarlyStopping(monitor='val_loss', patience=100)
mcp = ModelCheckpoint(filepath=model_name, monitor='val_loss', verbose=0, save_best_only=True)

history = model.fit(x, y, epochs=3500, batch_size=500, callbacks=[es, mcp], validation_split=0.2)

val_loss = history.history['val_loss']
accuracy = history.history['accuracy']

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

print('정확도는 파란색, 오차는 빨간색')
x_len = np.arange(len(accuracy))    # x축 범위

plt.figure()
plt.plot(x_len, val_loss, 'o', color='r', markersize=1)

plt.title('손실함수 그래프')
filename = 'wineCheckStop01.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

plt.figure()
plt.plot(x_len, accuracy, 'o', color='b', markersize=1)

plt.title('정확도 그래프')
filename = 'wineCheckStop02.png'
plt.savefig(filename)
print(filename + ' 파일 저장')