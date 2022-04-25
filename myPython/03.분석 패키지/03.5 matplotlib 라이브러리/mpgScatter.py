import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'mpg.csv'
myframe = pd.read_csv(filename, encoding='UTF-8')
print(myframe['drv'].unique())

mycolor = ['r', 'g', 'b']
labels = ['f', '4', 'r']
cnt = 0

for finditem in labels:
    xdata = myframe.loc[myframe['drv'] == finditem, 'displ']
    ydata = myframe.loc[myframe['drv'] == finditem, 'hwy']
    plt.plot(xdata, ydata, color=mycolor[cnt], linestyle='None', marker='o', label=finditem)
    cnt += 1

filename = 'mpgScatter.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')