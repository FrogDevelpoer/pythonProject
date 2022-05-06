filename = 'pima-indians-diabetes.csv'

import pandas as pd
data = pd.read_csv(filename)

print(data.columns)
print('-' * 30)
#
print(data.shape)
print('-' * 30)
#
# print(data.head())
# print('-' * 30)
#
print(data['class'].unique())
print('-' * 30)

concern = ['pregnant', 'plasma', 'pressure', 'thickness', 'insulin', 'bmi', 'pedigree', 'age']
x_data = data[concern]
y_data = data['class']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = \
    train_test_split(x_data, y_data, test_size=0.3)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
print('train 정확도 : %.3f' % train_score)
print('-' * 30)

test_score = model.score(x_test, y_test)
print('test 정확도 : %.3f' % test_score)
print('-' * 30)

print('기울기 : \n', model.coef_)
print('-' * 30)

print('절편 : \n', model.intercept_)
print('-' * 30)

import matplotlib
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False

plt.figure()

import numpy as np
from pandas import Series
myseries = Series(np.reshape(model.coef_, -1))
print(myseries)
print('-' * 30)

myseries.plot(kind='bar')

plt.title('독립변수들의 가중치')
plt.xticks(np.arange(len(concern)), concern, rotation='horizontal')

filename = 'logisticRegression03_01.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

test_prediction = model.predict(x_test)

print('confusion matrix')
from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, test_prediction)
print(cf_matrix)
print('-' * 30)

print('accuracy matrix')
from sklearn.metrics import accuracy_score
accuracy = 100 * accuracy_score(y_test, test_prediction)
print('accuracy : %.4f' % accuracy)
print('-' * 30)

print('classification_report')
from sklearn.metrics import classification_report
cl_report = classification_report(y_test, test_prediction)
print(cl_report)
print('-' * 30)

myframe = pd.DataFrame(cf_matrix)

# seaborn 라이브러리는 matplotlib의 서브 라이브러리
import seaborn as sns
sns.heatmap(myframe, annot=True, cmap='YlGnBu', fmt='g')

plt.xlabel('predict')
plt.ylabel('real data')
plt.title('confusion matrix')

filename = 'logisticRegression03_02.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

