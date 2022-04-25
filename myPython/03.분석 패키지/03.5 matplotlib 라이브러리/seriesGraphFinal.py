from pandas import Series
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

mylist = [30, 20, 40, 60, 50]
myindex = ['이상화', '한용운', '노천명', '윤동주', '이육사']
myseries = Series(data=mylist, index=myindex)
print(myseries)

mylim = [0, myseries.max() + 10]

myseries.plot(title='금월 실적', kind='line', rot=10, ylim=mylim)

filename='seriesGraphFinal.png'
plt.savefig(filename, dpi=400)
