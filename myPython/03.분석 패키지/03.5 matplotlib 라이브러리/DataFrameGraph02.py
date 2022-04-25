import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'ex802.csv'
myframe = pd.read_csv(filename, index_col='type', encoding='UTF-8')
myframe.index.name = '차량 유형'
myframe.columns.name = '도시(city)'
print(myframe)
print('-' * 30)

myframe.plot(kind='bar', rot=0, legend=False, title='지역별 차량 등록 현황')

filename = 'DataFrameGraph02_01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

myframeT = myframe.T

myframeT.plot(kind='bar', rot=0, legend=False, title='차량 유형별 등록 현황')
filename = 'DataFrameGraph02_02.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

ymax = myframeT.sum(axis=1)
print(ymax)
ymaxlimit = ymax.max() + 50

myframeT.plot(kind='bar', rot=0, ylim=[0, ymaxlimit], legend=True, title='차량 유형별 등록 현황', stacked=True)
filename = 'DataFrameGraph02_03.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')