import pandas as pd

filename = 'memberInfo.csv'
myframe = pd.read_csv(filename)
print(myframe)
print('-' * 30)

newdf01 = myframe.set_index(keys=['id'])
print(newdf01)
print('-' * 30)

newdf02 = myframe.set_index(keys=['id'], drop=False)
print(newdf02)
print('-' * 30)

myframe2 = pd.read_csv(filename, index_col='id')
print(myframe2)
print('-' * 30)

filename = 'memberInfo2.csv'
# header=None은 컬럼에 대한 헤더가 없음
# names를 통해서 컬럼에 대한 이름을 다시 지정해줄 수 있음
myframe2 = pd.read_csv(filename, header=None, names=['id', '국어', '영어'])
print(myframe2)
print('-' * 30)

filename = 'data02.csv'
myframe = pd.read_csv(filename, header=None, index_col=0, names=['학년', '국어', '영어', '수학'])
myframe.index.name = '이름'

myframe.loc[['강호민'], ['영어']] = 40
myframe.loc[['박영희'], ['국어']] = 30

print(myframe)
print('-' * 30)

df = myframe.astype({"영어": int}, errors='raise')
print(df)