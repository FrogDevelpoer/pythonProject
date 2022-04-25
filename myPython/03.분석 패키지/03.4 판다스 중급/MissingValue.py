import numpy as np
from pandas import Series

myseries = Series(['강감찬', '이순신', np.nan, '광해군'])
print(myseries)
print('-' * 30)

print(myseries.isnull())
print('-' * 30)

print(myseries.notnull())
print('-' * 30)

print(myseries[myseries.notnull()])
print('-' * 30)

# dropna 메소드는 누락된 데이터 배제
print(myseries.dropna())
print('-' * 30)

import pandas as pd
filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='UTF-8')
print(myframe)
print('-' * 30)

cleaned = myframe.dropna()
print(cleaned)
print('-' * 30)

cleaned = myframe.dropna(axis=1)
print(cleaned)
print('-' * 30)

cleaned = myframe.dropna(axis=0, subset=['영어'])
print(cleaned)
print('-' * 30)

cleaned = myframe.dropna(axis=0, how='all')
print(cleaned)
print('-' * 30)

cleaned = myframe.dropna(axis=1, how='all')
print(cleaned)
print('-' * 30)

myframe.loc[['강감찬', '홍길동'], ['국어']] = np.nan
print(myframe)
print('-' * 30)

cleaned = myframe.dropna(axis=1, how='all')
print(cleaned)
print('-' * 30)

# axis=1 이므로 열방향으로
# thresh=n은 의미있는 데이터가 n개 이상일 때 조회됨
cleaned = myframe.dropna(axis=1, thresh=1)
print(cleaned)
print('-' * 30)