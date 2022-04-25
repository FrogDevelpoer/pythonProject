import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series
# 5번 문제
plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# filename = 'ex802.csv'
# myframe = pd.read_csv(filename)
# print(myframe)
# print('-' * 30)
#
# myframe = myframe.set_index(keys='type')
#
# myframe.plot(kind='line', title='지역별 차종 교통량')
#
# filename = 'ex802.png'
# plt.savefig(filename, dpi=400)
# print(filename + ' 파일 저장')

# 7번문제
filename = 'mygraph.csv'
myframe = pd.read_csv(filename, index_col='이름')
print(myframe)

myframe.plot(kind='bar', title='학생별 누적 시험 점수', stacked=True, rot=0)

filename = 'mygraph.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')