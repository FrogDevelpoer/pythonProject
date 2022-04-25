from pandas import Series   # pandas에 있는 Series를 사용

mylist = [10, 20, 30]
myindex = ['뽕뺭', '너부리', '너구리']

myseries = Series(mylist)
print(myseries)
print('-' * 30)

myseries = Series(data=mylist)
print(myseries)
print('-' * 30)

myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-' * 30)

myseries = Series(data=mylist, index=myindex, dtype=float)
print(myseries)
print('-' * 30)