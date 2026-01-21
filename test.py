import sys
from collections import deque

def topology_sort():
    global queue
    result = []
    for i in range(1, v+1):
        if in_degree[i] == 0:
            queue.append(i)
            
    while queue:
        current = queue.popleft()
        result.append(current)
        for edge in directed_edge[current]:
            in_degree[edge]-=1
            if in_degree[edge] == 0:
                queue.append(edge)
                    
    return result
    

v, e = map(int, sys.stdin.readline().split())
directed_edge = [[] for _ in range(v+1)]
in_degree = [0]*(v+1)
for _ in range(e):
    a, b= map(int, sys.stdin.readline().split())
    directed_edge[a].append(b)
    in_degree[b]+=1
    
queue = deque()
print(*topology_sort())