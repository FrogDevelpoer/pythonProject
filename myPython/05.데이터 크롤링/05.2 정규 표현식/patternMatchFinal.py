import re

mylist = ['ab123', 'cd4#6', 'cf79a', 'abc1']

regex = '^[ac]{1}[0-9a-z]{4}$'    #\w{4}도 사용 가능
pattern = re.compile(regex)
totallist = []

for item in mylist:
    if pattern.match(item):
        print(item, '조건에 적합')
        totallist.append(item)
    else:
        print(item, '조건에 부적합')

print(totallist)
