import numpy as np
from pandas import Series, DataFrame

# 4번 문제
sdata = {
          '국어': [40, 60, 80, 50, 30],
          '영어': [55, 65, 75, 85, 60],
          '수학': [30, 40, 50, 60, 70]
        }
myindex = ['강감찬', '이순신', '김유신', '김구', '안중근']
myframe = DataFrame(sdata, index=myindex)
print(myframe)
print('-' * 30)

print(myframe.iloc[0::2])
print('-' * 30)

print(myframe.loc['이순신'])
print('-' * 30)

print(myframe.loc[['강감찬'], ['영어']])
print('-' * 30)

print(myframe.loc[['안중근', '강감찬'], ['국어', '수학']])
print('-' * 30)

myframe.loc['강감찬':'이순신', ['영어']] = 80
print(myframe)
print('-' * 30)

myframe.loc['이순신':'김구', ['수학']] = 100
print(myframe)
print('-' * 30)
print('-' * 30)

# 5번문제
myindex = ['윤봉길', '김유신', '신사임당']
mylist = [30, 40, 50]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-' * 30)

myindex = ['윤봉길', '김유신', '이순신']
mycolumns = ['용산구', '마포구', '서대문구']

mylist = list(3 * onedata for onedata in range(1, 10))
myframe = DataFrame(np.reshape(mylist, (3, 3)), index=myindex, columns=mycolumns)
print(myframe)
print('-' * 30)

myindex2 = ['윤봉길', '김유신', '이완용']
mycolumns2 = ['용산구', '마포구', '은평구']

mylist2 = list(5 * onedata for onedata in range(1, 10))
myframe2 = DataFrame(np.reshape(mylist2, (3, 3)), index=myindex2, columns=mycolumns2)
print(myframe2)
print('-' * 30)

result = myframe.add(myseries, axis=0)
print(result)
print('-' * 30)

result = myframe.add(myframe2, fill_value=0)
print(result)
print('-' * 30)

result = myframe.sub(myframe2, fill_value=0)
print(result)