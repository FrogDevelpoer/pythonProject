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
    # print(cur)

    sql = 'select * from region_summary_ranking '

    cur.execute(sql)

    cnt = []
    data = []
    total = 0

    for result in cur:
        total += result[1]
        data.append(result[1])
        cnt.append(result[0])
    # print(charData)
    newindex = []

    for idx in range(len(cnt)):
        newindex.append(cnt[idx] + '\n(' + str(round(100 * data[idx] / total, 2)) + '%)')
    print(newindex)

    charData = Series(data, index=newindex)
    charData.plot(kind='pie', title='지역별 ㄴ테러 발생 빈도(5~8위)')

    filename = 'terroroPie.png'
    plt.savefig(filename)
    print(filename + ' 파일 저장')

except Exception as err:
    print(err)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()