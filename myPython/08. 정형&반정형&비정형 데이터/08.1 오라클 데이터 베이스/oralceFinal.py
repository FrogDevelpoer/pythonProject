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

    sql = 'select bungi, mycount from bungitable order by ordering '
    cur.execute(sql)

    # print(cur)

    data = []
    bungi = []
    total = 0

    for result in cur:
        total += result[1]
        data.append(result[1])
        bungi.append(result[0])

    newindex = []
    for idx in range(len(bungi)):
        newindex.append(bungi[idx] + '\n(' + str(round(100 * data[idx] / total, 2)) + '%)')
    print(newindex)

    charData = Series(data, index=newindex)
    charData.plot(kind='pie', title='분기별 테러 빈도')

    filename = 'terror_pie.png'
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
