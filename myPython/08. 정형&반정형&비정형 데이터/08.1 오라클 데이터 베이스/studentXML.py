import cx_Oracle
from xml.etree.ElementTree import parse

conn = None
cur = None

xmlfile = 'mystudent.xml'
tree = parse(xmlfile)
myroot = tree.getroot()
# print(myroot)

try:
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo, encoding='UTF-8')
    mycursor = conn.cursor()

    students = myroot.findall('student')
    # print(len(students))

    for onestudent in students:
        total = float(onestudent[1].text) + float(onestudent[1].text) + float(onestudent[1].text)
        average = total / 3.0
        # print(average)
        sql = " insert into students"
        sql += " values('"
        sql += onestudent[0].text + "', '"
        sql += onestudent[1].text + "', '"
        sql += onestudent[2].text + "', '"
        sql += onestudent[3].text + "', '"
        sql += str(total) + "', '"
        sql += str(average) + "'"
        sql += " )"

        print(sql)
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