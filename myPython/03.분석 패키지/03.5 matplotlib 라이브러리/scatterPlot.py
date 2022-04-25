import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = '프로야구타자순위2021년.csv'
myframe = pd.read_csv(filename, encoding='UTF-8')
print(myframe.head())   # 데이터가 많은 경우 적당한 데이터만 볼 때 head 메소드 사용
print('-' * 30)

print(myframe.info())
print('-' * 30)

print(myframe['팀명'].unique())
print('-' * 30)

mycolors = ['r', 'g', 'b']
labels = ['두산', 'LG', '키움']
cnt = 0  # 색 관련 인덱스

for finditem in labels:
    xdata = myframe.loc[myframe['팀명'] == finditem, '안타']
    ydata = myframe.loc[myframe['팀명'] == finditem, '타점']
    plt.plot(xdata, ydata, color=mycolors[cnt], linestyle='None', marker='o', label=finditem)
    cnt += 1

plt.legend(loc=4)   # 4는 오른쪽 하단
plt.xlabel('안타 개수')
plt.ylabel('타점')
plt.title('안타와 타점에 대한 산점도')
plt.grid(True)

filename = 'scatterPlot02.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')