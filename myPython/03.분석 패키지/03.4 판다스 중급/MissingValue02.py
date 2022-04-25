import numpy as np
import pandas as pd

filename = 'excel01.csv'
myframe = pd.read_csv(filename, index_col='이름')
print(myframe)
print('-' * 30)

# inplace=False 옵션은 원본 데이터는 보존
print(myframe.fillna(0, inplace=False))
print('-' * 30)

print(myframe)
print('-' * 30)

myframe.fillna(0, inplace=True)
print(myframe)
print('-' * 30)

print('# inplace=True 적용 후')
print(myframe)
print('-' * 30)

myframe.loc[['강감찬', '홍길동'], ['국어', '영어']] = np.nan
myframe.loc[['박영희', '김철수'], ['수학']] = np.nan
print(myframe)
print('-' * 30)

mydict = {'국어': 15, '영어': 25, '수학': 35}
myframe.fillna(mydict, inplace=True)
print(myframe)
print('-' * 30)

myframe.loc[['박영희'], ['국어']] = np.nan
myframe.loc[['홍길동'], ['영어']] = np.nan
myframe.loc[['김철수'], ['수학']] = np.nan
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