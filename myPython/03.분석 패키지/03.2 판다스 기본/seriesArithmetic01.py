from pandas import Series, DataFrame

myindex1 = ['강호동', '유재석', '노홍철', '신동엽']
mylist1 = [30, 40, 50, 60]

myseries1 = Series(data=mylist1, index=myindex1)

myindex2 = ['강호동', '유재석', '노홍철', '이수근']
mylist2 = [20, 40, 60, 70]

myseries2 = Series(data=mylist2, index=myindex2)

print(myseries1)
print('-' * 10)

print(myseries2)
print('-' * 10)

# 시리즈 연산에는 방법1, 방법2 모두 사용 가능하다
print(myseries1 + 5)  # 방법 1
print('-' * 10)

print(myseries1.add(5))  # 방법 2  / sub, mul, div, floordiv
print('-' * 10)

print(myseries1 >= 40)
print('-' * 10)

newseries = myseries1 + myseries2
print(newseries)
print('-' * 10)

newseries = myseries1.sub(myseries2, fill_value=0)
print(newseries)
print('-' * 10)
