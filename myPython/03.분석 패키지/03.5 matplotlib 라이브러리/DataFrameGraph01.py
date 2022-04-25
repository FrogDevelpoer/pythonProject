import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'dataframeGraph.csv'
myframe = pd.read_csv(filename, encoding='euc-kr')
print(myframe)
print('-' * 30)

myframe = myframe.set_index(keys='name')
print(myframe)
print('-' * 30)

# legend : 범례
# figsize : 도화지 크기
myframe.plot(kind='line', title='직원별 지역 실적', legend=True, figsize=(10, 6))

filename = 'DataFrameGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')