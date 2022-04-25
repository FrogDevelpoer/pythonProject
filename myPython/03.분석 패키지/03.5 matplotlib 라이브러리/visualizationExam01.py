import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

theaterfile = 'theater.csv'
colname = ['id', 'theater', 'region', 'bindo']
dftheater = pd.read_csv(theaterfile, header=None, names=colname)

dftheater = dftheater.rename(index=dftheater.id)
dftheater = dftheater.reindex(columns=['theater', 'region', 'bindo'])
dftheater.index.name = 'id'

print(dftheater.head())
print('극장 별 상영 집계 횟수')
mygrouping = dftheater.groupby('theater')['bindo']

sumseries = mygrouping.sum()
print(sumseries)
print('-' * 30)

meanseries = mygrouping.mean()
print(meanseries)
print('-' * 30)

sizeseries = mygrouping.size()
print(sizeseries)
print('-' * 30)

df = pd.concat([sumseries, meanseries, sizeseries], axis=1)
df.columns = ['합계', '평균', '개수']
print(df)

mysize = len(mygrouping.groups)     # 그룹 수

df.plot(kind='barh', rot=0)
plt.title(str(mysize) + '개 매장 집계 데이터')

filename = 'visualizationExam01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

print('집계 메소드를 사전에 담아 전달하기')
print('지역의 개수와 상영횟수의 총합')

# agg : aggregate의 줄임말
mydict = {'bindo': ['sum', 'mean'], 'region': 'size'}
result = dftheater.groupby('theater').agg(mydict)
print(result)
print('-' * 30)

import numpy as np

print('numpy를 이용한 방법')
result = mygrouping.agg([np.count_nonzero, np.mean, np.std])
print(result)
print('-' * 30)

from math import sqrt

def myroot(values):
    # 총합에 root를 사용하여 리턴
    mysum = sum(values)
    return sqrt(mysum)

def plus_add(values, somevalue):
    # 총합에 root를 사용하고 somevalue를 더해주는 함수
    result = myroot(values) + somevalue
    return result

mygrouping = dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 같이 쓰기')
result = mygrouping.agg(myroot)
print(result)
print('-' * 30)

print('groupby와 사용자 정의 함수(매개변수 2개) 같이 쓰기')
result = mygrouping.agg(plus_add, somevalue=3)
print(result)
print('-' * 30)

print('컬럼 2개 이상을 그룹화 하기')
newgrouping = dftheater.groupby(['theater', 'region'])['bindo']
result = newgrouping.count()
print(result)
print('-' * 30)