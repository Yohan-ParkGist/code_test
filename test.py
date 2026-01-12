import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
plus, minus, multi, div = map(int, sys.stdin().readline().split())

operator = []
results = []

def dfs(index, plus, minus, multi, div):
    if index == len(operator):
        results.append(operator[:])
        return
    
    if plus>0:
        dfs(index+1, plus-1, minus, multi, div)
    if minus>0:
        dfs(index+1, plus, minus-1, multi, div)
    if multi>0:
        dfs(index+1, plus, minus, multi-1, div)
    if div>0:
        dfs(index+1, plus, minus, multi, div-1)
        
        