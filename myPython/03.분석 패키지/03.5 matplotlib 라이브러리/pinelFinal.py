import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

mycolors = ['blue', '#6AFF00', 'yellow', '#FF003C', 'green']
mylist = [30, 20, 40, 60, 50]
myindex = ['이상화', '한용운', '노천명', '윤동주', '이육사']

plt.pie(x=mylist, labels=myindex, colors=mycolors, counterclock=False, startangle=90, autopct='%1.2f%%', explode=(0, 0.1, 0, 0, 0))

filename = 'pinelFinal.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')