from pandas import Series
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

mylists = [30, 20, 40, 30, 60, 50]
myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주', '홍길동']
myseries = Series(data=mylists, index=myindex)
print(myseries)
print('-' * 30)

myylim = [-10, myseries.max() + 10]

myseries.plot(title='시험 점수', kind='line', grid=True, rot=10, use_index=True, ylim=myylim)
# plt.show()

filename = 'seriesGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')