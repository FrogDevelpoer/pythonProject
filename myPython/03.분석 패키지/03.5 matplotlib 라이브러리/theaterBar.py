import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'theater.csv'
colname = ['id', 'theater', 'region', 'bindo']
myframe = pd.read_csv(filename, header=None, names=colname)
print(myframe)
print('-' * 30)

myframe = myframe.rename(index=myframe.id)
myframe = myframe.reindex(columns=['theater', 'region', 'bindo'])
myframe.index.name = 'id'

print(myframe.head())
print('-' * 30)

mygrouping = myframe.groupby('region')['bindo']
sumseries = mygrouping.sum()
print(sumseries)
print('-' * 30)

meanseries = mygrouping.mean()
print(meanseries)
print('-' * 30)

sizeseries = mygrouping.size()
print(sizeseries)
print('-' * 30)

df = pd.concat([sumseries, meanseries, sizeseries], axis=1)
df.columns = ['합계', '평균', '개수']

df.plot(kind='bar', rot=0)

filename = 'theaterBar.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')