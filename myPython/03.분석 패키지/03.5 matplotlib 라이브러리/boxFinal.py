import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'mpg.csv'
myframe = pd.read_csv(filename, encoding='UTF-8')

frame01 = myframe.loc[myframe['drv'] == 'f', 'hwy']
frame01.index.name = '전륜 구동'
print(frame01.head())
print('-' * 30)

frame02 = myframe.loc[myframe['drv'] == '4', 'hwy']
frame02.index.name = '4륜 구둥'
print(frame02.head())
print('-' * 30)

frame03 = myframe.loc[myframe['drv'] == 'r', 'hwy']
frame03.index.name = '후륜 구동'
print(frame03.head())
print('-' * 30)

totalframe = pd.concat([frame01, frame02, frame03], ignore_index=True, axis=1)
totalframe.columns = ['f', '4', 'r']
print(totalframe.head())

totalframe.plot(kind='box')

plt.xlabel('구동방식')
plt.ylabel('주행 마일수')
plt.title('고속도로 주행 마일수의 상자 수염')

filename = 'mpg.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')