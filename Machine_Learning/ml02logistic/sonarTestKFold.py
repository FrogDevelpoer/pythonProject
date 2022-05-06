filename = 'sonarTest.csv'

import pandas as pd
df = pd.read_csv(filename, header=None)

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

n_fold = 10  # 교차할 겹의 갯수
seed = 0

from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

cost = []   # for Loss value(손실 함수)
accuracy = []   # for accuracy(정확도)

cnt = 0     # 카운터 변수

for train, test in skf.split(x, y):
    cnt += 1
    print(str(cnt) + '번째 실행중')
    model = Sequential()
    model.add(Dense(units=24, activation='relu', input_dim=x_column))
    model.add(Dense(units=10, activation='relu'))
    model.add(Dense(units=y_column, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(x[train], y[train], epochs=200, batch_size=5)

    # 학습 완료 후 테스트 데이터를 이용하여 평가를 진행
    score = model.evaluate(x[train], y[train])
    cost.append(score[0])
    accuracy.append(score[1])
# end for

print('손실 함수')
print(cost)
print('-' * 30)

print('손실 함수의 평균')
print('%.3f' % (sum(cost) / n_fold))
print('-' * 30)

print('정확도')
print(accuracy)
print('-' * 30)

print('정확도의 평균')
print('%.3f' % (sum(accuracy) / n_fold))
print('-' * 30)

