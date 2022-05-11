menu = int(input('순차 복사(0), 랜덤 복사(1) : '))

if menu == 0:
    target_folder = '../datasets/cats_and_dogs_small'
else:
    target_folder = '../datasets/cats_and_dogs_random'
# end if

import os
train_folder = os.path.join(target_folder, 'train')
validation_folder = os.path.join(target_folder, 'validation')

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

TARGET_WIDTH, TARGET_HEIGHT = 150, 150
BATCH_SIZE = 20

# 케라스 모델에 사용할 Generator 객체 생성
train_generator = train_datagen.flow_from_directory(
                    directory=train_folder,
                    target_size=(TARGET_WIDTH, TARGET_HEIGHT),
                    batch_size=BATCH_SIZE,
                    class_mode='binary'
                )

validation_generator = validation_datagen.flow_from_directory(
                    directory=validation_folder,
                    target_size=(TARGET_WIDTH, TARGET_HEIGHT),
                    batch_size=BATCH_SIZE,
                    class_mode='binary'
                )

for data_batch, label_batch in train_generator:
    # (배치 사이즈, TARGET_WIDTH, TARGET_HEIGHT, color_mode)
    print('배치 데이터 크기 : ', data_batch.shape)     # (20, 150, 150, 3)
    print('배치 데이터(정답) 크기 : ', label_batch.shape)
    break

# 모델을 생성하곡 학습을 진행
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from tensorflow.python.keras.callbacks import EarlyStopping

model = Sequential()

COLOR_MODE = 3  # 컬러 이미지
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(TARGET_WIDTH, TARGET_HEIGHT, COLOR_MODE)))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(units=512, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

es = EarlyStopping(patience=3, monitor='val_loss')
history = model.fit(
    x=train_generator,
    steps_per_epoch=100,
    epochs=30,
    validation_data=validation_generator,
    validation_steps=50,
    verbose=1,
    callbacks=[es]
)

accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

import matplotlib.pyplot as plt

x = range(len(accuracy))

plt.figure()
plt.plot(x, accuracy, 'bo', label='training accuracy')
plt.plot(x, val_accuracy, 'b', label='validation accuracy')
plt.title('training and validation accuracy')
plt.legend(loc='best')
filename = 'catAndDog03_01.png'
plt.savefig(filename)
print(filename + ' 파일 저장 완료')

plt.figure()
plt.plot(x, loss, 'bo', label='training loss')
plt.plot(x, val_loss, 'b', label='validation loss')
plt.title('training and validation loss')
plt.legend(loc='best')
filename = 'catAndDog03_02.png'
plt.savefig(filename)
print(filename + ' 파일 저장 완료')

print('fin')