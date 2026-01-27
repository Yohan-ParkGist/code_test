import sys

n = int(sys.stdin.readline())

r, c = map(int, sys.stdin.readline().split())
rank = []
rank.append(r)
rank.append(c)

for _ in range(n-1):
    r, c = map(int, sys.stdin.readline().split())
    rank.append(r)
    rank.append(c)

dp = [[[0]*(n+1) for _ in range(n+1)]]

for diagonal in range(2, n+1):
    for i in range(1, n-diagonal+2):
        j = i + diagonal - 1
        for p in range(i, j):
            dp[i][j] = min()