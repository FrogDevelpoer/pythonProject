from pandas import Series

# 문제 2번
myindex = ['강감찬', '이순신', '김유신', '광해군', '연산군', '을지문덕']
mylist = [50, 60, 40, 80, 70, 20]

myseries = Series(data=mylist, index=myindex)

print(myseries)
print('-' * 30)

myseries[1] = 100
myseries[2:5] = 999
myseries[['강감찬', '을지문덕']] = 30
print(myseries)
print('-' * 30)

# 문제 3번
myindex1 = ['성춘향', '이몽룡', '심봉사']
mylist1 = [40, 50, 60]
myseries01 = Series(data=mylist1, index=myindex1)

print(myseries01)
print('-' * 30)

myindex2 = ['성춘향', '이몽룡', '뺑덕어멈']
mylist2 = [20, 40, 70]
myseries02 = Series(data=mylist2, index=myindex2)

print(myseries02)
print('-' * 30)

addseries = myseries01.add(myseries02, fill_value=0)
print(addseries)
print('-' * 30)

subseries = myseries01.sub(myseries02, fill_value=0)
print(subseries)