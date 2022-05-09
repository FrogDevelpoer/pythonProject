import pandas as pd

filename = 'titanic.csv'
data = pd.read_csv(filename)
print(data.shape)
print('-' * 30)

print(data.columns)
print('-' * 30)

print(data['survived'].unique())
print('-' * 30)

print(data['sex'].unique())
print('-' * 30)

# 코딩 변경 : 적합한 데이터 분석을 위하여 데이터의 값을 인위적으로 변경하는 작업(re-coding)
data['sex'] = data['sex'].map({'female': 1, 'male': 0})
print(data['sex'].unique())
print('-' * 30)

# 결측치 존재 여부 확인
print(data['age'].unique())
print('-' * 30)

print(data['age'].value_counts())
print('-' * 30)

# 결측치 처리 : 비어있는 age 컬럼은 평균으로 대체
data['age'].fillna(value=data['age'].mean(), inplace=True)
print('-' * 30)

print(data['pclass'].unique())
print('-' * 30)

# 더미 코딩 : 해당 승객이 어떤 클래스(1, 2, 3 등석)에 승선했는가를 표현하기 위하여 신규 컬럼 생성
data['firstclass'] = data['pclass'].apply(lambda x: 1 if x == 1 else 0)
data['secondclass'] = data['pclass'].apply(lambda x: 1 if x == 2 else 0)

print(data.columns)
print('-' * 30)

concern = ['sex', 'age', 'firstclass', 'secondclass']
x_data = data[concern]
y_data = data['survived']

print('x_data\n', x_data)
print('-' * 30)

print('y_data\n', y_data)
print('-' * 30)

from sklearn.model_selection import train_test_split
seed = 1234
x_train, x_test, y_train, y_test = \
    train_test_split(x_data, y_data, test_size=0.3, random_state=seed)

# 표준화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# 로지스틱 모델 생성
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
print('train accuracy : %.4f' % train_score)
print('-' * 30)

test_score = model.score(x_test, y_test)
print('train accuracy : %.4f' % test_score)
print('-' * 30)

print('학습 이후의 회귀계수')
print('기울기: \n', model.coef_)
print('절편: \n', model.intercept_)
print('-' * 30)

'''
['sex',         'age',      'firstclass', 'secondclass'
 [[ 1.27547829 -0.45986584  0.97211399  0.48698546]]
 성별과 일등석 컬럼에 대한 가중치 계수가 큼
 이 2개의 컬럼이 생존 여부에 큰 인과 관계를 가짐
 연장자일수록 생존 확률이 낮아짐
'''

# 가중치 정보를 이용한 시각화
import matplotlib
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False

from pandas import Series
import numpy as np
myseries = Series(np.reshape(model.coef_, -1))  # 데이터 1차원화 이후 시리즈로 만들기

plt.figure()
myseries.plot(kind='bar')

plt.title('독립 변수 가중치')
plt.xticks(np.arange(len(concern)), concern, rotation='horizontal')

filename = 'logisticRegression02_01.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

# 샘플용 데이터 만들기
#             sex, age, firstclass, secondclass
soo = np.array([0.0, 20.0, 0.0, 0.0])
hee = np.array([1.0, 17.0, 1.0, 0.0])
minho = np.array([0.0, 32.0, 1.0, 0.0])
sample = np.array([soo, hee, minho])

print(sample)
print('-' * 30)

print('예측값 확인')
prediction = model.predict(sample)
print(prediction)
print('-' * 30)

print('확률 확인')
prediction_proba = model.predict_proba(sample)
print(prediction_proba)
print('-' * 30)

print('최대 인덱스 찾기')
argmax = np.argmax(prediction_proba, axis=1)
print(argmax)
print('-' * 30)

print('test result')
test_prediction = model.predict(x_test) # 테스트에 대한 예측 정보

# 실제 정답(y_test)과 에측정보(test_prediction)에 대한 각 정보 확인
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
cf_matrix = confusion_matrix(y_test, test_prediction)
print(cf_matrix)
print('-' * 30)

accuracy = accuracy_score(y_test, test_prediction)
print('정확도 : %.4f' % (100.0 * accuracy))
print('-' * 30)

cl_report = classification_report(y_test, test_prediction)
print('클래스 리포트')
print(cl_report)
print('-' * 30)


import seaborn as sns
import pandas as pd
plt.figure()
myframe = pd.DataFrame(cf_matrix)
sns.heatmap(myframe, annot=True, cmap='YlGnBu', fmt='g')

plt.title('confusuion matrix')
plt.xlabel('prediction')
plt.ylabel('real(label)')

filename = 'logisticRegression02_02.png'
plt.savefig(filename)
print(filename + ' 파일 저장')
