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

    name = []
    bindo = []

    for result in cur:
        name.append(result[0])
        bindo.append(result[1])
    charData = Series(bindo, index=name)
    # print(charData)

    charData.plot(kind='barh', rot=0)
    plt.title('지역별 테러 발생 빈도(5~8위)')
    filename = 'terrorBar.png'
    plt.savefig(filename)
    print(filename + ' 파일 저장')

except Exception as err:
    print(err)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()