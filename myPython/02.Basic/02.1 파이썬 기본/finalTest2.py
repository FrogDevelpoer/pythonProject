# 품목 이름, 수량, 단가를 입력받아 총 금액 구하기
name = input('이름 : ')
qty = int(input('수량 : '))
price = int(input('단가 : '))

result = qty * price

print('이름 : %s' % name)
print('수량 : %d' % qty)
print('단가 : %d' % price)
print('총 금액 : %d' % result)


