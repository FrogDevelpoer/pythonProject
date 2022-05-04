filename='surgeryTest.csv'

import numpy as np
data=np.loadtxt(filename, delimiter=',')

print('type(data) :', type(data))
print('data.shape :', data.shape)

table_col = data.shape[1] # 데이터 컬럼 개수
y_column = 1 # 정답을 가지고 있는 컬럼 수
x_column = table_col - y_column # 입력되는 컬럼 개수

# 환자의 기록과 수술 결과를 x, y변수에 따로 저장합니다.
x = data[:, 0:x_column]
y = data[:, x_column:(x_column+1)]

print('x.shape :', x.shape)
print('y.shape :', y.shape)

from sklearn.model_selection import train_test_split

# seed = 0
# x_train, x_test, y_train, y_test = \
#     train_test_split(x, y, test_size=0.2, random_state=seed)

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2)

from tensorflow.python.keras.models import Sequential
model = Sequential()

from tensorflow.python.keras.layers import Dense
model.add(Dense(units=30, input_dim=x_column, activation='relu'))

model.add(Dense(units=y_column, activation='sigmoid'))

# metrics는 측정 지표라고 합니다.
# 정확도(accuracy)에 대하여 살펴 보고자 합니다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=30, batch_size=10)

print('model.inputs')
print(model.inputs)
print('model.outputs')
print(model.outputs)
print('model.layers')
print(model.layers)

print(model.metrics_names)

# 평가를 진행합니다.
score = model.evaluate(x_train, y_train)
print('train loss : %.4f' % (score[0]))
print('-'*30)

print('train accuracy : %.4f' % (score[1]))
print('-'*30)

pred = model.predict(x_test)
print('pred')
print(pred)
print('-'*30)

# argmax 함수는 배열에서 가장 큰 요소가 들어 있는 색인 번호를 반환합니다.
prediction = np.argmax(pred, axis=-1)
print('prediction')
print(prediction)
print('-'*30)

print('실제 정답과 예측 값 동시 출력하기')
for idx in range(len(prediction)):
    label = y_test[idx]
    print('real : %f, prediction : %f' % (label, prediction[idx]))

print('산술 연산으로 정확도를 구해 봅니다.')
print('전체 개수 : %d' % len(prediction))

hit_count = 0 # 맞춘 개수
for idx in range(len(prediction)):
    hit_count += np.sum(prediction[idx] == y_test[idx])

print('맞춘 개수 : %d' % hit_count)

accuracy = 100.0 * (hit_count / len(prediction))
print('정확도 : %.4f' % accuracy )

print('evaluate 함수를 사용하면 쉽게 손실 비용과 정확도를 구할 수 있습니다.')
score = model.evaluate(x_test, y_test)
print('test loss : %.4f' % (score[0]))
print('test accuracy : %.4f' % (score[1]))

print('finished')