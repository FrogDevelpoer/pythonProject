mystring = 'i am very tired'

# split() : 스페이스를 구분자로 문자열을 나누어 list로 만들어줌
mylist = mystring.split(' ')

for idx in range(len(mylist)):
    if idx % 2 == 0:
        mylist[idx] = mylist[idx].upper()
    else:
        mylist[idx] = mylist[idx].lower()

print('조인 함수 사용하기')
result = ' # '.join(mylist)

print(result)
