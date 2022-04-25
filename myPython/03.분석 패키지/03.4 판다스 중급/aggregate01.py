import numpy as np
from pandas import DataFrame

mydata = [[10.0, np.nan, 0], [20.0, 30.0, 40.0], [np.nan, np.nan, np.nan], [40.0, 50.0, 30.0]]
myindex = ['이순신', '김유신', '윤봉길', '홍길동']
mycolumn = ['국어', '영어', '수학']
myframe = DataFrame(data=mydata, index=myindex, columns=mycolumn)
print(myframe)
print('-' * 30)

# 집계 함수는 기본적으로 결측치 값을 배제하고 연산
print(myframe.sum(axis=0))
print('-' * 30)

print(myframe.sum(axis=1))
print('-' * 30)

print(myframe.mean(axis=1, skipna=False))
print('-' * 30)

print(myframe.mean(axis=1, skipna=True))
print('-' * 30)

print(myframe.max(axis=1, skipna=False))
print('-' * 30)

print(myframe.max(axis=1, skipna=True))
print('-' * 30)

print(myframe.idxmax())     # 과목별 점수가 가장 높은 인덱스 반환
print('-' * 30)

print(myframe.cumsum(axis=0))
print('-' * 30)

print(myframe.cumsum(axis=1))   # 좌측부터 우측으로 합을 누적
print('-' * 30)

# cumprod : 누적 곱셈, cummax / cummin : 값 중에서 최대/최소 요소만 추출

print(myframe)
print('-' * 30)

myframe.loc[myframe['국어'].isnull(), '국어'] = myframe['국어'].mean()
myframe.loc[myframe['수학'].isnull(), '수학'] = myframe['수학'].mean()
myframe.loc[myframe['영어'].isnull(), '영어'] = myframe['영어'].mean()

print(myframe)
print('-' * 30)

print(myframe.describe())
print('-' * 30)

print(myframe.info())
print('-' * 30)