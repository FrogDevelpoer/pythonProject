# 2번 문제
import numpy as np
from pandas import DataFrame

mydata = [[60.0, np.nan, 90.0], [np.nan, 80.0, 50.0], [40.0, 50.0, np.nan]]
myindex = ['강감찬', '김유신', '이순신']
mycolumns = ['국어', '영어', '수학']
myframe = DataFrame(data=mydata, index=myindex, columns=mycolumns)
print(myframe)
print('-' * 30)

mydict = {
            '국어': myframe['국어'].mean(),
            '영어': myframe['영어'].mean(),
            '수학': myframe['수학'].mean()
}
myframe.fillna(mydict, inplace=True)
print(myframe)

print('-' * 30)
print('-' * 30)
print('-' * 30)

# 3번 문제
import pandas as pd

filename = '과일매출현황.csv'
myframe = pd.read_csv(filename)
print(myframe)
print('-' * 30)

mydict = {'구입액': 50.0, '수입량': 20.0}
myframe.fillna(mydict, inplace=True)
print(myframe)