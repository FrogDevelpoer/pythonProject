import numpy as np
from pandas import DataFrame

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군']
mycolumns = ['서울', '부산', '광주', '목포', '경주']
mylist = list(onedata * 10 for onedata in range(1, 26))
# print(mylist)

myframe = DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumns)
print(myframe)
print('-' * 30)

result = myframe.iloc[1]    # 숫자 기반의 로케이션
print(result)
print(type(result))
print('-' * 30)

result = myframe.iloc[[1, 3]]
print(result)
print(type(result))
print('-' * 30)

result = myframe.iloc[0::2]     # 짝수 번째의 요소만 반환
print(result)
print('-' * 30)

result = myframe.loc['이순신']     # 문자 기반의 로케이션
print(result)
print('-' * 30)

result = myframe.loc[['이순신']]
print(result)
print('-' * 30)

result = myframe.loc[['이순신', '강감찬']]    # ,은 떨어져 있는 경우에 사용 :은 연속적인 데이터에 사용
print(result)
print('-' * 30)

result = myframe.loc[['강감찬'], ['광주']]
print(result)
print('-' * 30)

result = myframe.loc[['강감찬', '연산군'], ['광주', '목포']]
print(result)
print('-' * 30)

result = myframe.loc['김유신':'광해군', '광주':'목포']
print(result)
print('-' * 30)

result = myframe.loc['김유신':'광해군', ['부산']]
print(result)
print('-' * 30)

result = myframe.loc[[False, True, True, False, True]]
print(result)
print('-' * 30)

result = myframe.loc[myframe['부산'] <= 100]
print(result)
print('-' * 30)

result = myframe.loc[myframe['목포'] == 140]
print(result)
print('-' * 30)

# result = myframe.loc[myframe['부산'] >= 70 & myframe['목포'] >= 140]
cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140
df = DataFrame([cond1, cond2])
print(df)
print('-' * 30)

print(df.all())
print('-' * 30)

print(df.any())
print('-' * 30)

result = myframe.loc[df.all()]
print(result)
print('-' * 30)

result = myframe.loc[lambda df: df['광주'] >= 130]
print(result)
print('-' * 30)
# 이까지 Read

# 아래부터 Write
myframe.loc[['이순신', '강감찬'], ['부산']] = 30
print(myframe)
print('-' * 30)

myframe.loc['김유신':'광해군', ['경주']] = 80
print(myframe)
print('-' * 30)

myframe.loc['연산군', :] = 50      # :는 모든 열을 의미
print(myframe)
print('-' * 30)

myframe.loc[:, '광주'] = 60      # :는 모든 행을 의미
print(myframe)
print('-' * 30)

myframe.loc[myframe['경주'] <= 60, ['경주', '광주']] = 0
print(myframe)
print('-' * 30)
print('-' * 30)
print('-' * 30)