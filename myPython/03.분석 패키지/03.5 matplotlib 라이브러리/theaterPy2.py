import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'theater.csv'
colname = ['id', 'theater', 'region', 'bindo']
myframe = pd.read_csv(filename, header=None, names=colname)

myframe = myframe.rename(index=myframe.id)
myframe = myframe.reindex(columns=['theater', 'region', 'bindo'])
myframe.index.name = 'id'

print(myframe.head())

mygrouping = myframe.groupby('theater')['bindo']
sumseries = mygrouping.sum()
print(sumseries)

mycolors = ['red', 'blue']
mylist = [160, 160]
myindex = ['cgv', 'magabox']

plt.pie(x=mylist, labels=myindex, colors=mycolors, autopct='%1.2f%%')

filename = 'theaterPy2.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')