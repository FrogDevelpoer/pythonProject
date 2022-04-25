def nolambda(x, y):
    return 3 * x + 2 * y


x, y = 3, 5
result = nolambda(x, y)
print(result)

# yeslambda = lambda 매개변수 : 구현할 내용
yeslambda = lambda x, y: 3 * x + 2 * y

result = yeslambda(x, y)
print(result)
