import sys

def matrix_mul(matrix1, matrix2):
    ans = [[0]*dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            for l in range(dim):
                ans[i][j] += matrix1[i][l]*matrix2[l][j]
                ans[i][j] = ans[i][j]%p
    return ans

def mat_power(a, b):
    if b == 1:
        for i in range(dim):
            for j in range(dim):
                a[i][j] %= p
        return a
    temp = (mat_power(a, b//2))
    if b%2 == 0:
        return matrix_mul(temp, temp)
    else:
        return matrix_mul(a, matrix_mul(temp, temp))

dim = 2
n = int(sys.stdin.readline())
p = 1000000007

matrix = [[1, 1], [1, 0]]

final = mat_power(matrix, n)

print(final[0][1])