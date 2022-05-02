import cx_Oracle
from xml.etree.ElementTree import parse

conn = None
cur = None

xmlfile = 'xmlEx_04_total.xml'
tree = parse(xmlfile)
myroot = tree.getroot()
# print(myroot)
# print('-' * 30)

try:
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    mycursor = conn.cursor()
    # print(mycursor)
    # print('-' * 30)

    items = myroot.findall('item')
    # print(len(items))

    for oneitem in items:
        sql = "insert into shops"
        sql += " values('"
        sql += oneitem[0].text + "', '"
        sql += oneitem[1].text + "', '"
        sql += oneitem[2].text + "', '"
        sql += oneitem[3].text + "', '"
        sql += oneitem[4].text + "', '"
        sql += oneitem[5].text + "', '"
        sql += oneitem[6].text + "', '"
        sql += oneitem[7].text + "' "
        sql += " )"

        print(sql)
        print('-' * 30)

        mycursor.execute(sql)

    conn.commit()
except Exception as err:
    if conn is not None:
        conn.rollback()
    print(err)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()

print('fin')