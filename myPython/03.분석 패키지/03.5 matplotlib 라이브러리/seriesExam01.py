import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

myindex = ['강감찬', '홍길동', '이순신', '최영']
members = Series(data=[20, 60, 80, 40], index=myindex)
print(members)
members.plot(title='국어 점수', kind='bar', rot=0, ylim=[0, 100], color=['r', 'g', 'b', 'y'])

plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.title('학생들 국어 시험')

ratio = 100 * members / members.sum()

for idx in range(members.size):
    value = str(members[idx]) + '건'     # 예시 : 20건
    ratioval = '%.1f%%' % (ratio[idx])  # 예시 : 20.0%
    plt.text(x=idx, y=members[idx] + 1, s=value, horizontalalignment='center')

    plt.text(x=idx, y=members[idx] / 2, s=ratioval, horizontalalignment='center')

meanval = members.mean()
average = '평균 %d건' % meanval

plt.axhline(y=meanval, color='red', linewidth='2', linestyle='dashed')

# x, y는 좌표, s는 보여줄 문자열
plt.text(x=0, y=meanval+1, s=average, horizontalalignment='center')


filename = 'graph01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')