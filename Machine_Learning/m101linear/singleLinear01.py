import numpy as np

filename = 'singleLinear01.csv'
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

# 2. 레이어 추가하기
# add 메소드는 모델 객채에 레이어를 추가해주는 역할을 한다.
# Dense 객체는 각 레이어에 디하여 어떠한 구조를 만들어주는 역할을 함
from tensorflow.python.keras.layers import Dense
model.add(Dense(units=y_column, input_dim=x_column, activation='linear'))
'''
Dense 객체는 각 레이어에 대하여 어뚸한 구조를 만들어 주는 역할
units : 출력 값의 크기(output의 수). 값이 30이면 30개의 노드를 생성한다는 의미
input_dim : 입력 데이터로부터 몇 개의 데이터가 들어올지를 결정
activation : 사용할 활성화 함수 지정. 기본 값은 linear로 선형 회귀를 의미
'''

# 3. 컴파일 하기
# 모델이 효과적으로 구현될 수 있도록 컴파일 해주는 메소드
model.compile(loss='mean_squared_error', optimizer='adam')
'''
loss : 문자열 형식의 비용(손실) 함수 이름 지정
optimizer : 문자열 형식의 옵티마이저를 지정
'''

# 4. 모델 실행 시키기
# epochs 숫자 만큼 훈련을 시켜 실제로 모델을 실행시켜주는 메소드
model.fit(x_train, y_train, epochs=10000, batch_size=10000, verbose=1)
'''
epochs: 정수 값, 모델을 학습시키기 위한 epoch 숫자를 의미
batch_size : 정수 값, None, 기본 값은 32. 샘플을 한번에 몇개씩 처리할지 정의하는 부분
verbose : (값) 설명
- (0)은 출력하지 않음
- (1)vaildation_split 비율을 제외한 나머지 항목을 progress_bar를 포함시켜 출력(기본 값)
- (2)epoch 당 1번만 출력
'''

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

filename = 'singleLinear01.png'
plt.savefig(filename)

print('테스트 데이터로 예측해보기')
prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx]
    pred = prediction[idx]  # 테스트용 데이터를 사용한 예측치

    print('정답 : %.4f, 예측값 : %.4f' % (label, pred))
print('fin')