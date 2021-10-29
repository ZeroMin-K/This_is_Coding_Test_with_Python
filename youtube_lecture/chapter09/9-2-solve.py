INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# k번 회사를 거쳐 x번으로 
x, k = map(int, input().split())

for q in range(1, k+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][q] + graph[q][j])


if graph[x][k] == INF:
    print(-1)
else:
    print(graph[x][k])
