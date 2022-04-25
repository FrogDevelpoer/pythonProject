import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

slices = [1, 2, 3, 4]
hobbies = ['잠자기', '외식', '영화 감상', '운동']
mycolors = ['blue', '#6AFF00', 'yellow', '#FF00CC']

plt.pie(x=slices, labels=hobbies, colors=mycolors, counterclock=False, startangle=90, autopct='%1.2f%%', shadow=True, explode=(0, 0.1, 0, 0))

filename = 'pieGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')