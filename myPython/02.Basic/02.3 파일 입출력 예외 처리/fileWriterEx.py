# text = ' 강호동,60.0,70.0,80.0,M'
# result = text.strip().split(',')
# print(result)
#
# kor = float(result[1])
# print(kor+5)

myfile01 = open('sample03.txt', 'rt', encoding='UTF-8')
linelists = myfile01.readlines()
myfile01.close()

myfile02 = open('result03.txt', 'wt', encoding='UTF-8')

for one in linelists:
    mylist = one.strip().split(',')
    name = mylist[0]
    total = float(mylist[1]) + float(mylist[2]) + float(mylist[3])
    _gender = mylist[4]
    if _gender == 'M':
        gender = '남자'
    else:
        gender == '여자'

    text = name + '/' + str(total) + '/' + gender
    myfile02.write(text + '\n')

myfile02.close()
