import sys
import heapq

def bellman_ford(init, n):
    s = []
    distance = [float('inf')]*(n+1)
    distance[init] = 0
    heapq.heappush(s, (0, init))
    while s:
        dist, u = heapq.heappop(s)
        if distance[u] < dist:
            continue
        
        for edge in edge_weight[u]:
            cost = dist+edge[1]
            if distance[edge[0]] > cost:
                distance[edge[0]] = cost
                heapq.heappush(s, (cost, edge[0]))
                
    return distance



v, e = map(int, sys.stdin.readline().split())
edge_weight = [[] for _ in range(v+1)]
distance = [float('inf')]*(v+1)
k = int(sys.stdin.readline())
for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    edge_weight[a].append((b, w))

bellman_ford(k, v)

for i in range(1, v+1):
    print(distance[i])