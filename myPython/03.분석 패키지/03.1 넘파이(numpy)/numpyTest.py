import numpy as np

# 3번
print(np.ones(4))
print('-' * 30)

arrZeros = np.zeros((2, 3))
print(arrZeros)
print('-' * 30)

arrOnes = np.ones((3, 3))
print(arrOnes)
print('-' * 10)

# 4번
a = np.array([-1, 3, 3, -6, 3, 0])
b = np.array([3, 6, 1, 2, 0, 2])

A = np.reshape(a, [2, 3])
B = np.reshape(b, [3, 2])
print(A)
print('-' * 10)
print(B)
print('-' * 10)
result3_1 = np.matmul(A, B)
result3_2 = np.matmul(B, A)
print(result3_1)
print(result3_2)