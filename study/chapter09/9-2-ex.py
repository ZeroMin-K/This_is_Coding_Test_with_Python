# 무한을 의미하는 값으로 10억 설정
INF = int(1e9)

# 노드의 개수 및 간선 개수 입력
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    # a와 b가 서로에게 가는 비용 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 k, 최종 목적지 노드 x입력
k, x = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1 출력
if distance >= INF:
    print(-1)
# 도달할 수 있으면 최단 거리 출력
else:
    print(distance)