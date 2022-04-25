from pandas import Series

myindex = ['용산구', '마포구', '영등포구', '금천구', '서대문구', '광진구', '은평구']

mylist = [50, 60, 40, 80, 70, 30, 20]

myseries = Series(data=mylist, index=myindex)
print(myseries)

print('\n색인의 이름으로 읽기')
print(myseries['서대문구'])

print('\n색인의 이름으로 읽기')
print(myseries[['서대문구']])

print('\n라벨 이름으로 슬라이싱')
print(myseries['서대문구':'은평구'])

print('\n서로 떨어진 데이터를 추출')
print(myseries[['서대문구', '은평구']])

print('\n정수를 이용한 데이터 추출')
print(myseries[2])

print('\n짝수번째 데이터 읽기')
print(myseries[0:5:2])

print('\n홀수번째 데이터 읽기')
print(myseries[1:8:2])

print('시리즈 개수 : ' + str(myseries.size))

myseries[2] = 90
myseries[2:5] = 33

myseries[['서대문구', '용산구']] = 55

myseries[0::2] = 80

print('\n')
print(myseries)
