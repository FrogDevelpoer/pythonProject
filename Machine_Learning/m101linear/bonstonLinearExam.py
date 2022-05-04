from keras.datasets import boston_housing

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()
'''
(404, 13) : x_train 데이터의 shape
(404,) : y_train 데이터의 shape
(102, 13) : x_test 데이터의 shape
(102,) : y_test 데이터의 shape
'''

# print(x_train.shape)
# print('-' * 30)
#
# print(y_train.shape)
# print('-' * 30)
#
# print(x_test.shape)
# print('-' * 30)
#
# print(y_test.shape)
# print('-' * 30)

# EarlyStopping : 훈련 데이터의 학습이 계속 진행되어도 더 이상 오차가 줄지 않으면 강제로 학습을 멈추게 하는 callback 함수

input_dim = x_train.shape[1]
print('입력 데이터 열 개수 : ' + str(input_dim))
print('입력 데이터 개수 : ' + str(len(x_train)))
print('출력 데이터 개수 : ' + str(len(x_test)))

print('0번째 데이터 정보')
print(x_train[0])
print(y_train[0])

# 데이터 전처리
x_mean = x_train.mean(axis=0)   # 평균
x_std = x_train.std(axis=0)     # 표준 편차
x_train -= x_mean   # 해당 요소를 평균으로 뺄셈
x_train /= x_std    # 표준 편차로 나누기
x_test -= x_mean
x_test /= x_std

y_mean = y_train.mean(axis=0)   # 평균
y_std = y_train.std(axis=0)     # 표준 편차
y_train -= y_mean   # 해당 요소를 평균으로 뺄셈
y_train /= y_std    # 표준 편차로 나누기
y_test -= y_mean
y_test /= y_std

print('0번째 데이터 정보(표준화 이후)')
print(x_train[0])
print(y_train[0])

response = int(input('Early Stopping 사용(1), 미사용(2) : '))

# 모델 생성 및 데이터 학습

from tensorflow.python.keras.models import Sequential
model = Sequential()
##############################################################################
y_column = 1

from tensorflow.python.keras.layers import Dense
model.add(Dense(units=y_column, input_shape=(input_dim,), activation='linear'))

##############################################################################
# mse = mean_squared_error
model.compile(loss='mse', optimizer='adam')
model.summary()  # 모델의 설정 정보 간략히 보기

##############################################################################
from tensorflow.python.keras.callbacks import EarlyStopping

if response == 1:
    # patience=100 : 100 epoch동안 모니터링한 평가 지표가 개선되지 않으면 Stop
    # 'Loss' : 훈련 데이터의 손실 비용, 'val_loss': 검증용 데이터의 손실 비용
    # val_loss를 확인하려면 fit 메소드에 validation_split 매개 변수를 명시 해주어야 함
    # validation_split : 훈련이 잘되는지 검증하는 용도로 데이터들을 분리하는 비율
    # monitor='val_loss' : 검증용 데이터에 대한 비용 함수를 모니터링
    # history : fitting 해 본 정보들을 저장하고 있는 객체로, 'loss' 정보와 'val_loss' 정보를 확인할 수 있음
    es = EarlyStopping(patience=100, monitor='val_loss')
    history = model.fit(x_train, y_train, epochs=5000, batch_size=32, callbacks=[es], validation_split=0.25)
else:
    history = model.fit(x_train, y_train, epochs=5000, batch_size=32, validation_split=0.25)

loss = history.history['loss']
val_loss = history.history['val_loss']

# print(loss)
# print('-' * 30)

# print(val_loss)
# print('-' * 30)

##############################################################################
# 데이터 시각화

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

plt.figure()
plt.plot(loss, 'b', label = 'training data loss', linestyle='solid', linewidth=1)
plt.plot(val_loss, 'r', label='validation data loss', linestyle='solid', linewidth=1)

plt.xlabel('epochs')
plt.ylabel('loss value')
plt.title('회귀 모델 학습 시각화')
plt.legend()

filename = 'boston01.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

##############################################################################

print('실제 가격과 예측 가격의 산점도')
prediction = model.predict(x_test & y_test)

plt.figure()
plt.plot(y_test, prediction, 'b.')

# y = x 직선 그리기
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], ls='--', c='.3')

plt.xlabel('real data')
plt.ylabel('prediction data')
plt.title('실제 가격 vs 예측 가격')

filename = 'boston02.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

