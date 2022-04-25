coffee = 3
price = 2000

print('판매 가능한 커피 잔량 : %d' % coffee)
print('단가 : %d원' % price)

while True:
    money = int(input('돈을 넣어주세요 : '))
    if money == price:
        print('커피를 판매 합니다')
        coffee -= 1
    elif money > price:
        coffee -= 1
        print('거스름돈 {}원을 주고, 1잔을 판매했습니다.'.format(money - price))
    else:
        print('금액이 부족합니다.')

    print('남은 커피의 양은 {}잔 입니다.'.format(coffee))

    if coffee == 0:
        print('커피가 매진되었습니다.')
        break

