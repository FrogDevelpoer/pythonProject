import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

csv_file = 'allStoreModified.csv'
myframe = pd.read_csv(csv_file, encoding='UTF-8', index_col=0)
# print(myframe.head())
# print('-' * 30)

# print(myframe['brand'].unique())
# print('-' * 30)

mycolor = ['r', 'g', 'b', 'm']
brand_dict = {'cheogajip': '처갓집', 'goobne': '굽네', 'nene': '네네', 'pelicana': '페리카나'}

seoulframe = myframe.loc[myframe['sido'] == '서울특별시']
kkframe = myframe.loc[myframe['sido'] == '경기도']

newframe = pd.concat([seoulframe, kkframe], axis=0)
print(newframe)

mygrouping = newframe.groupby(['brand'])['brand']

chartdata = mygrouping.count()

chartdata.index = [brand_dict[idx] for idx in chartdata.index]
print(chartdata)
print('-' * 30)



plt.figure()    # 각각 다른 그래프를 만들 때 서로 엉키는 것을 방지하기 위함
chartdata.plot(kind='bar', legend=False, color=mycolor, rot=0, title='서울/경기 점포 개수')
filename = 'makeChickenGraph02Final.png'
plt.savefig(filename)

print(filename + 'fin')