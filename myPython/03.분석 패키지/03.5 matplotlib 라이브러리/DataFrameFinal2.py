import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 6번 문제
myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주']
mylist = [30, 20, 40, 30, 60]
myframe2 = Series(data=mylist, index=myindex)
print(myframe2)
myframe2.plot(title='학생별 시험 점수', kind='bar', rot='0')

plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.title('학생별 시험 점수')

ratio = 100 * myframe2 / myframe2.sum()

for idx in range(myframe2.size):
    value = str(myframe2[idx]) + '점'
    ratioval = '%.1f%%' % (ratio[idx])
    plt.text(x=idx, y=myframe2[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=myframe2[idx] / 2, s=ratioval, horizontalalignment = 'center')

meanval = myframe2.mean()
average = '평균 %d점' % meanval

plt.axhline(y=meanval, color='black', linewidth=2, linestyle='dashed')

plt.text(x=0, y=meanval+1, s=average, horizontalalignment='center')

filename = 'dfFinal.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')