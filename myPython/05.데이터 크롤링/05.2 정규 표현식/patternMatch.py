import re

# 소문자 2개 숫자 3개로 구성된 항목 찾기
mylist = ['ab123', 'cd456', 'ef789', 'abc12']

regex = '[a-z]{2}\d{3}' # 정규식
pattern = re.compile(regex)

totallist = []   # 조건에 맞는 항목들만 넣기

for item in mylist:
    if pattern.match(item):
        print(item, '은(는) 조건에 적합')
        totallist.append(item)
    else:
        print(item, '은(는) 조건에 부적합')

print(totallist)