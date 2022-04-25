from pandas import Series

mylist = [10, 40, 30, 20]
myseries = Series(data=mylist, index=['맹꽁이', '맹공이', '너부리', '너구리'])

print(type(myseries))
print('-' * 10)

print(myseries)
print('-' * 10)

myseries.index.name = '점수'      # 색인의 이름
print(myseries)
print('-' * 10)

myseries.name = '학생들 점수'
print(myseries)
print('-' * 10)

print(myseries.index)
print('-' * 10)

print(myseries.values)
print('-' * 10)

for idx in myseries.index:
    print('색인 : ' + idx, ', 값 : ' + str(myseries[idx]))