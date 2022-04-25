from pandas import Series

mylist = [200, 300, 400, 100]
myseries = Series(data=mylist, index=['손오공', '저팔계', '사오정', '삼장법사'])

print('#시리즈의 색인 이름')
myseries.index.name = '실적 현황'
print(myseries)

print('#시리즈의 이름')
myseries.name = '직원 실적'
print(myseries)

print('#반복하여 출력해보기')
for idx in myseries.index:
    print('색인 : ' + idx, ', 값 : ' + str(myseries[idx]))