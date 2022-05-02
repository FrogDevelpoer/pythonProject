import cx_Oracle
import matplotlib.pyplot as plt
from pandas import Series

plt.rc('font', family='Malgun Gothic')

conn = None
cur = None

try:
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    cur = conn.cursor()

    sql = 'select * from three_country '
    cur.execute(sql)

    name = []   # 발생 국가
    year = []    # 발생 년도
    bindo = []  # 발생 빈도

    for result in cur:
        name.append(result[0])
        year.append(result[1])
        bindo.append(result[2])

    chartData = Series(bindo, index=[name, year])
    print(chartData)
    print('-' * 30)

    for idx in range(0, 2):
        myframe = chartData.unstack(idx)
        myframe.plot(kind='barh', rot=0)
        plt.title('3개국 테러 현황')
        filename = 'oracleChart02_0' + str(idx+1) + '.png'
        plt.savefig(filename)
        print(filename + ' 파일 저장')

except Exception as err:
    print(err)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

print('fin')
