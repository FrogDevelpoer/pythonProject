# 정수 1개를 입력받아 짝수이면 제곱, 홀수이면 3제곱 출력
a = int(input('정수 입력 : '))

if a % 2 == 0:
    print(a * a)
else:
    print(a * a * a)



