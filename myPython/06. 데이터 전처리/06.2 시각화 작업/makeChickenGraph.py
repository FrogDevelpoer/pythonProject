import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

csv_file = 'allStoreModified.csv'
myframe = pd.read_csv(csv_file, encoding='UTF-8', index_col=0)
print(myframe.head())
print('-' * 30)

print(myframe['brand'].unique())
print('-' * 30)

mycolor = ['r', 'g', 'b', 'm']
brand_dict = {'cheogajip': '처갓집', 'goobne': '굽네', 'nene': '네네', 'pelicana': '페리카나'}

mygrouping = myframe.groupby('brand')['brand']

chartdata = mygrouping.count()

newindex = [brand_dict[idx] for idx in chartdata.index]

chartdata.index = newindex

print(chartdata)
print('-' * 30)

plt.figure()    # 각각 다른 그래프를 만들 때 서로 엉키는 것을 방지하기 위함

chartdata.plot(kind='pie', legend=False, colors=mycolor, autopct='%1.2f%%')
filename = 'makeChickenGraph01.png'
plt.savefig(filename)

print(filename + 'fin')

plt.figure()

chartdata.plot(kind='bar', legend=False, color=mycolor, rot=0, title='브랜드별 매장 개수')
filename = 'makeChickenGraph02.png'
plt.savefig(filename)

print(filename + 'fin')