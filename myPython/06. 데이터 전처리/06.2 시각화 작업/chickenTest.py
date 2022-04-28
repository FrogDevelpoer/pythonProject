import pandas as pd
import matplotlib.pyplot as plt

colnames = ['지역', '브랜드', '매장수']
chickenfile = 'chicken.csv'
myframe = pd.read_csv(chickenfile, names=colnames, header=None)
print(myframe)
print('=' * 30)

mygrouping = myframe.groupby('브랜드')['매장수']
print(type(mygrouping))
print('=' * 30)

myseries = mygrouping.sum()
print(myseries)
print('=' * 30)

plt.rcParams['font.family'] = 'Malgun Gothic'

mycolor = ['red', 'green', 'blue']
mytitle = '브랜드별 매장 개수'
myylim = [0, myseries.max() + 5]
myalpha = 0.7   # 투명도

myseries.plot(kind='bar', rot=0, title=mytitle, legend=False, ylim=myylim, alpha=myalpha, color=mycolor)
plt.show()
print('fin')