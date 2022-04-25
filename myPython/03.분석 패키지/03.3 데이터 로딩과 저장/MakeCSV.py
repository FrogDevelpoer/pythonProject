import random # 랜덤 데이터를 생성해주는 모듈
import pandas as pd

result = []
mycolumns = ('번호', '이름', '나이')
myencoding = 'UTF-8'

for idx in range(1, 3):
    sublist = []
    sublist.append(100 * idx)
    sublist.append('김철수' + str(idx))
    sublist.append(random.randint(1, 10))
    result.append(sublist)

print(result)

myframe = pd.DataFrame(result)
filename = 'csv_01_01.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=True)

filename = 'csv_01_02.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False)

filename = 'csv_01_03.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, header=False)

filename = 'csv_01_04.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, sep='%')

print('fin')