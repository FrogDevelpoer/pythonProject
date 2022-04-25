import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

slices = [15, 30, 20, 25]
id = ['brother', 'hulk', 'king', 'lucky']
mycolor = ['green', 'aqua', 'red', 'purple']

plt.pie(x=slices, colors=mycolor, autopct='%1.1f%%', labels=id)

filename = 'theaterPy.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')