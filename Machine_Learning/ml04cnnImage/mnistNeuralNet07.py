from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# CNN은 데이터를 4차원 형상으로 변경햏주어야 한다.

x_column = 28 * 28
x_train = x_train.reshape((60000, 28, 28, 1))     # 형상 변경
x_train = x_train.astype(float)/255

x_test = x_test.reshape((10000, 28, 28, 1))
x_test = x_test.astype(float)/255

print('before y_train[0]')
print(y_train[0])

from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

print('after y_train[0]')
print(y_train[0])

# 모델 생성 후 학습
from tensorflow.python.keras.models import Sequential
model = Sequential()

nb_classes = 10

from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout

model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dense(units=512, input_shape=(x_column,), activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(units=nb_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print('model.fit 진행중')
history = model.fit(x_train, y_train, validation_split=0.3, epochs=5, batch_size=64)

print('history의 모든 데이터 목록 보기')
print(history.history.keys())

print('model을 평가합니다.')
score = model.evaluate(x_test, y_test, verbose=1)
print(score)
print('-' * 30)

print('평가 지표 목록')
print(model.metrics_names)
print('-' * 30)

print('test loss : %.4f' % (score[0]))
print('test accuracy : %.4f' % (score[1]))

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
# 정확도에 대한 데이터 시각화
plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(['train', 'test'], loc='upper left')

filename = '../ml03softmax/mnistNeuralNet06_01.png'
plt.savefig(filename)
print(filename + ' 저장 완료')

# 손실 함수에 대한 데이터 시각화
plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'test'], loc='upper left')

filename = '../ml03softmax/mnistNeuralNet06_02.png'
plt.savefig(filename)
print(filename + ' 저장 완료')