import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
filename = 'theater.csv'
colname = ['id', 'theater', 'region', 'bindo']

myframe = pd.read_csv(filename, names=colname)
myframe = myframe.drop(columns='region')
result = myframe[myframe['theater'] == 'daehan'].index
df2 = myframe.drop(result)
print(df2)
print('-' * 30)

mydict = {'bindo': 'sum'}
result2 = df2.groupby('id').agg(mydict)
print(result2)
print('-' * 30)

idslice = list(result2.index)
valslice = result2.values
valslice = np.hstack(valslice)

plt.pie(x=valslice, labels=idslice, autopct='%.1f%%')

filename = 'theaterPy3.png'
plt.axis('equal')
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')