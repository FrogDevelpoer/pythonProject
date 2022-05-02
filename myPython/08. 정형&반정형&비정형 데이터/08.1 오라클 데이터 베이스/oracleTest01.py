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
    # print(conn)

    sql = 'select * from top_10 '
    cur.execute(sql)

    data = []   # 테러 숫자
    country = []    # 발생 국가

    for result in cur:
        data.append(result[1])
        country.append(result[0])

    mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FF00F0', '#CCFFEE', '#05FCA2', '#1F2E3D']
    chartData = Series(data, index=country)

    # print(chartData)
    chartData.plot(kind='bar', rot=18, title='테러 빈도 TOP 10 국가', color=mycolor, alpha=0.7)

    plt.ylabel('빈도수', rotation=0)

    filename = 'oracleChart01.png'
    plt.savefig(filename)
    print(filename + ' 파일 저장')

    import pandas as pd
    myframe = pd.read_sql(sql, conn, index_col='COUNTRY_TXT')
    print(myframe)
    print('- * 50')

except Exception as err:
    print(err)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

print('fin')
