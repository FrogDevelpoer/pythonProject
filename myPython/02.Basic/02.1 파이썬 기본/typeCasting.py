# 현재 3가지 모두 문자형
str1 = '100'
str2 = '200'
str3 = '12.345'

# 문자형을 정수형, 실수형으로 변환
int1 = int(str1)
int2 = int(str2)
float1 = float(str3)

print(int1 == str)

sum = int1 + int2
print('출력1 : ', sum)

float2 = float1 + 35.2
print('출력2 : ', float2)

print(type(str1))
print(type(int1))
print(type(float1))
