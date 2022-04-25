tuple01 = (10, 20, 30)
tuple01 = tuple01 + (40, )  # 40을 튜플형식으로 만들어주려면 , 를 붙혀줘야 한다.

print(tuple01)
print(type(tuple01))

# 이렇게도 작성 가능
tuple02 = 10, 20, 30, 40
print(tuple02)
print(type(tuple02))

mylist = [10, 20, 30, 40]
tuple03 = tuple(mylist)

if tuple02 == tuple03:
    print('equal')
else:
    print('different')

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)

# +기호로 튜플을 합쳐줄 수 있음
tuple06 = tuple04 + tuple05
print(tuple06)

# *기호로 튜플을 지정한 수 만큼 반복
tuple07 = tuple04 * 5
print(tuple07)

# swap 기법
a, b = 11, 22
a, b = b, a
print('a = ', a, 'b = ', b)

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3])
print(tuple08[3:])

# 튜플은 원소의 값 변경x
