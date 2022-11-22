# 무한을 의미하는 값 - 10억 설정
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현) 생성, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기
for a in range(1, n + 1):
    graph[a][a] = 0 

# 각 간선에 대한 정보 입력받아 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    if count == n:
        result += 1

print(result)