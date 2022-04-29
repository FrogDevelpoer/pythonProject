from xml.etree.ElementTree import parse

tree = parse('mystudent.xml')
myroot = tree.getroot()
# print(myroot)

students = myroot.findall('student')
print(students)

for onestudent in students:
    print('이름: ', onestudent[0].text)
    print('국어: ', onestudent[1].text)
    print('수학: ', onestudent[2].text)
    print('영어: ', onestudent[3].text)
    print('-' * 30)