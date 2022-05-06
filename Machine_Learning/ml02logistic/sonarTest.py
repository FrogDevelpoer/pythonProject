filename='sonarTest.csv'

import pandas as pd
df=pd.read_csv(filename, header=None)

# print(df.head())
# print('-'*30)
#
# print(df.info())
# print('-'*30)
#
# print(df[60].unique())
# print('-'*30)

data = df.values
table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
# y_raw는 분류 문자열 'R'과 'M' 중에 하나의 값으로 되어 있습니다.
# LabelEncoder 클래스를 사용하여 숫자형 데이터로 변형이 필요합니다.
y_raw = data[:, x_column:].ravel()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(y_raw)
y = le.transform(y_raw)

# 다음과 같이 실수형으로 변환해야 합니다.
# import numpy as np
x = x.astype(float)
y = y.astype(float)

print('y_raw[0:10] :\n', y_raw[0:10])
print('y[0:10] :\n', y[0:10])

from sklearn.model_selection import train_test_split
seed=0
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=seed)

from tensorflow.python.keras.models import Sequential
model = Sequential()

from tensorflow.python.keras.layers import Dense
model.add(Dense(units=24, activation='relu', input_dim=x_column))
model.add(Dense(units=10, activation='relu'))
model.add(Dense(units=y_column, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=200, batch_size=5)

print('모델을 파일로 저장합니다.')
model_name = 'my_model.h5'
model.save(model_name)

del model # 메모리 내의 모델 객체를 삭제합니다.

print('모델을 다시 로딩합니다.')
from tensorflow.python.keras.models import load_model
model = load_model(model_name)

score = model.evaluate(x_test, y_test)
print('test loss : %.4f' % (score[0]))
print('test accuracy : %.4f' % (score[1]))

print('finished')

