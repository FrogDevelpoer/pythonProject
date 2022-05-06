filename = 'iris.csv'

import pandas as pd
data = pd.read_csv(filename)

# print(data.columns)
# print('-' * 30)
#
# print(data.shape)
# print('-' * 30)
#
# print(data.head())
# print('-' * 30)
#
# print(data['Name'].unique())
# print('-' * 30)

x_data = data[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y_data = data['Name']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = \
    train_test_split(x_data, y_data, test_size=0.3)

# print('before x_train\n', x_train)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# fit transform() : 평균과 표준 편차를 사용하여 표준화를 수행하고, 변형 작업을 수행
x_train = scaler.fit_transform(x_train)

# transform() : fit() 기능을 제외하고 fit_transform()메소드와 동일한 기능을 수행
x_test = scaler.transform(x_test)

# print('after x_train\n', x_train)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
# print('train 정확도 : %.3f' % train_score)
# print('-' * 30)

test_score = model.score(x_test, y_test)
# print('test 정확도 : %.3f' % test_score)
# print('-' * 30)

# print('기울기 : \n', model.coef_)
# print('-' * 30)
#
# print('절편 : \n', model.intercept_)
# print('-' * 30)

# 샘플 데이터와 모델을 사용하여 데이터 예측하기
import numpy as np

sample = np.array([[5.0, 3.0, 1.2, 0.1], [6.1, 2.9, 4.3, 1.2], [7.7, 3.0, 6.4, 1.9]])
sample = scaler.transform(sample)

# 오류 확인
##########################################################################################
print('에측 값 확인')
prediction = model.predict(sample)
print(prediction)
print('-' * 30)
##########################################################################################

print('확률로 보기')
predict_proba = model.predict_proba(sample)
print(predict_proba)
print('-' * 30)

print('최대 인덱스 찾기')
print(np.argmax(predict_proba, axis=1))
print('-' * 30)

print('test result')
test_prediction = model.predict(x_test)

# y_test : 실제 정답
# test_prediction : 테스트 데이터로 예측할 결과(예측치)

print('confusion matrix')
from sklearn.metrics import confusion_matrix

cf_matrix = confusion_matrix(y_test, test_prediction)
print(cf_matrix)
print('-' * 30)

print('accuracy matrix')
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, test_prediction)
print(accuracy)
print('-' * 30)

print('classification_report')
from sklearn.metrics import classification_report
cl_report = classification_report(y_test, test_prediction)
print(cl_report)
print('-' * 30)

# seaborn 라이브러리는 matplotlib의 서브 라이브러리

myframe = pd.DataFrame(cf_matrix)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

import seaborn as sns
sns.heatmap(myframe, annot=True, cmap='YlGnBu', fmt='g')

plt.xlabel('predict')
plt.ylabel('real data')
plt.title('confusion matrix')

filename = 'logistic01.png'
plt.savefig(filename)
print(filename + ' 파일 저장')