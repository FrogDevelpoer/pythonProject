import numpy as np
from pandas import Series, DataFrame

myindex = ['강호동', '유재석', '이수근']
mylist = [30, 40, 50]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-' * 30)

myindex = ['강호동', '유재석', '이수근']
mycolumns = ['서울', '부산', '경주']

mylist = list(10 * onedata for onedata in range(1, 10))

myframe = DataFrame(np.reshape(mylist, (3, 3)), index=myindex, columns=mycolumns)
print(myframe)
print('-' * 30)

# 위 내용을 이용하여 산술연산하기
print(myframe)
print('-' * 30)

print('dataframe + series')
result = myframe.add(myseries, axis=0)
print(result)
print('-' * 30)

myindex2 = ['강호동', '유재석', '김병만']
mycolumns2 = ['서울', '부산', '대구']

mylist2 = list(5 * onedata for onedata in range(1, 10))

myframe2 = DataFrame(np.reshape(mylist2, (3, 3)), index=myindex2, columns=mycolumns2)
print(myframe2)
print('-' * 30)

result = myframe.add(myframe2)
print(result)
print('-' * 30)

result = myframe.add(myframe2, fill_value=0)
print(result)
print('-' * 30)

# sub, mul, div