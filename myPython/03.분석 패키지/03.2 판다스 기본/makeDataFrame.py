import numpy as np
from pandas import DataFrame

mydata = np.arange(9).reshape((3, 3))
print(mydata)

myframe = DataFrame(data=mydata, index=['용산구', '마포구', '은평구'], columns=['뽕뺭', '너부리', '너구리'])
print(myframe)

sdata = {'지역': ['용산구', '마포구'], '년도': [2019, 2020]}      # 딕셔너리와 리스트 중첩
myframe = DataFrame(data=sdata)
print(myframe)

sdata = {'용산구': {2020: 10, 2021: 20}, '마포구': {2020: 30, 2021: 40, 2022: 50}}     # 딕셔너리의 중첩(튜플도 가능)
myframe = DataFrame(data=sdata)
print(myframe)

sdata = {
            '지역': ['용산구', '용산구', '용산구', '마포구', '마포구'],
            '년도': [2019, 2020, 2021, 2020, 2021],
            '실적': [20, 30, 35, 45, 55]
        }
myframe = DataFrame(data=sdata)
print(myframe)
