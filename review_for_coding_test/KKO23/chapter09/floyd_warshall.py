INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받아 그값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용 
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우 무한 출력
        if graph[a][b] == INF:
            print('INIFINITY', end=' ')
        # 도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end = ' ')
    print()
