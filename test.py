import sys

n, m = map(int, sys.stdin.readline().split())
memory = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[float('inf')]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = 0
    for j in range(1, m+1):
        if memory[i] >= j:
            dp[i][j] = min(dp[i-1][j], cost[i])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-memory[i]]+cost[i])
            
print(dp[n][m])