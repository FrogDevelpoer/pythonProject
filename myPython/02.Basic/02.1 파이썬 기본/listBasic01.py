somelist = ['짜장면', '짬뽕', '탕수육', '칠리새우', '깐풍기', '치킨', '피자']
print(somelist)

print(somelist[4])
print(somelist[-2])
print(somelist[1:4])
print(somelist[4:])

length = len(somelist)
print('요소 개수 : ', length)

# 슬라이싱[시작:종점:증강치]
print(somelist[1:length:2])
print(somelist[0:length:2])
