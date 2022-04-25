mylist1 = list(onedata for onedata in range(1, 6))      # onedata : 단수 개념 range(1, 6) : 복수 개념   / range의 값인 1부터 5까지를 onedata에 넣고 이를 리스트 형태로 바꿈
# mylist01 = list((1, 2, 3, 4, 5))
# mylist01 = [1, 2, 3, 4, 5]
# 위 3가지는 모두 같은 의미
print(mylist1)

# 1~6의 값이 있는 리스트에서 각 값들에 10 곱하기
mylist2 = list(10 * onedata for onedata in range(1, 6))     # 리스트 값에 산술하기 : onedata 앞에 산술 작성
print(mylist2)


# 배열의 값들을 제곱한 값중 짝수만 출력
mylist3 = [3, 4, 6, 2]
result = [idx ** 2 for idx in mylist3 if idx % 2 == 0]
print(result)
