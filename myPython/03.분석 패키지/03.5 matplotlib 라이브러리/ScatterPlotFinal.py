import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'tips.csv'
myframe = pd.read_csv(filename)
print(myframe)

mycolor = ['r', 'b']
labels = myframe['sex'].unique()
cnt = 0

for finditem in labels:
    xdata = myframe.loc[myframe['sex'] == finditem, 'total_bill']
    ydata = myframe.loc[myframe['sex'] == finditem, 'tip']
    plt.plot(xdata, ydata, color=mycolor[cnt], linestyle='None', marker='o', label=finditem)
    cnt += 1

plt.legend()
plt.title('결제 총액과 팁 비용의 산점도')
plt.xlabel('결제 총액')
plt.ylabel('팁 비용')
filename = 'tips.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')