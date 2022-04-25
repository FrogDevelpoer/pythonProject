coffee = 3
price = 2000

print('우리 매장에는 커피가 {}잔이 있습니다.'.format(coffee))

money = int(input('돈을 넣어주세요 : '))
print('{}원을 입금하셨습니다.'.format(money))

change = money - price
print('거스름돈은 {}원 입니다.'.format(change))
print('남은 커피는 {}잔 입니다.'.format(coffee - 1))
