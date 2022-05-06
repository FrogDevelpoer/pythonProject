import numpy as np

filename = 'singleLinear02.csv'
data = np.loadtxt(filename, delimiter=',')
# print(type(data))
# print(data)

table_col = data.shape[1]   # 열의 개수

y_column = 1    # 데이터 컬럼 수
x_column = table_col - y_column    # 입력 데이터 컬럼 수

x = data[:, 0:x_column]
y = data[:, x_column:]

# print('x : ', x)
# print('-' * 30)
#
# print('y : ', y)
# print('-' * 30)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=1/4, random_state=0)   # 입력, 출력, 테스트 수치(25%)

# print('x_train : ', x_train)
# print('-' * 30)
#
# print('x_test : ', x_test)
# print('-' * 30)
#
# print('y_train : ', y_train)
# print('-' * 30)
#
# print('y_test : ', y_test)
# print('-' * 30)
############################################################################

# Keras Part
# 1. 모델 객체 생성하기
# Sequential 모델은 레이어를 선형으로 연결하여 모델을 구성해준다
from tensorflow.python.keras.models import Sequential

model = Sequential()    # 객체 생성


from tensorflow.python.keras.layers import Dense
model.add(Dense(units=y_column, input_dim=x_column, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')


# 4. 모델 실행 시키기
# epochs 숫자 만큼 훈련을 시켜 실제로 모델을 실행시켜주는 메소드
model.fit(x_train, y_train, epochs=10000, batch_size=10000, verbose=1)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

plt.title('회귀선과 산점도 그래프')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x_train, y_train, 'k.')    # 산점도

train_pred = model.predict(x_train)
plt.plot(x_train, train_pred, 'r')    # 최적합 회귀선 그리기

print('가중치 정보(w, b)')
print(model.get_weights())

filename = 'singleLinear02.png'
plt.savefig(filename)

print('테스트 데이터로 예측해보기')
prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx]
    pred = prediction[idx]  # 테스트용 데이터를 사용한 예측치

    print('정답 : %.4f, 예측값 : %.4f' % (label, pred))
print('fin')