import cx_Oracle

conn = None     # 접속 객체
cur = None      # 커서 객체

try:
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    print(type(conn))

    cur = conn.cursor()
    # print(type(cur))

    sql = 'select power(2, 10) from dual'
    cur.execute(sql)

    for item in cur:
        print(item)

except Exception as err:
    print(err)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()

print('fin')