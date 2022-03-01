import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

x, k = map(int, input().split())


for p in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][p] + graph[p][b])

result = graph[a][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)