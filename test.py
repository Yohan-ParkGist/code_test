import sys

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()
n = len(word1)
m = len(word2)
lcs = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if word1[j-1] == word2[i-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    
print(lcs[m][n])