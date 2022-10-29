"""
n개의 도시(2 <= n <= 100)
한 도시에 출발하여 다른 도시에 도착하는 m개 버스(1 <= m <= 100,000)
각 버스는 한번 사용할때 비용있음
(A,B)쌍에 대해 도시 A에서 B로 가는 필요한 비용의 최솟값 계산

a->b 비용 c
노선이 하나가 아닐수도있음. 

i번째 줄에 출력하는 j번째 숫자도시 i에서 j로 가는 최소비용
갈수없으면 0출력 
플로이드워셜 알고리즘 사용

"""

# 무한대
INF = int(1e9)

# 도시개수 n입력
n = int(input())
# 버스개수 m 입력
m = int(input())

# 각 도시에 도착하는 경우 2차원 리스트 생성 
graph = [[INF] * n for _ in range(n)]

# 자기자신으로 가는 경로 0으로초기화
for i in range(n):
    graph[i][i] = 0

#m번반복하며
for _ in range(m):
    # 버스 정보 입력 - 시작도시a, 도착도시b, 한번타는데 필요비용 c (비용 c는 10000보다 작거나 가은 수)
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c

print(graph)

# 플로이드 워셜 알고리즘 사용
# k번째를 경우하는 경우(0부터 n까지 n반복)
for k in range(n):
    # 도시 i부터 출발하며(0부터 n까지 n반복)
    for i in range(n):
        # 도시 j까지 도착하는 경우 (0부터 n까지 n 반복)
        for j in range(n):
            # i-> j까지 가는최소 비용 = i-> j까지 가는 최소비용, i->k->j까지 가는 최소 경우중 가장 작은 비용
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][k])

# i 출발해서  - 0부터 n까지 반복하며
for i in range(n):
    # j 까지 도착하는 경우- 0부터 n까지 반복하며
    for j in range(n):
        # 도달할 수 없는 경우
        if graph[i][j] == INF:
            # 0출력
            print('0', end=' ')
        # 도달할 수 있는 경우 
        else:
            # [i][j] 비용 출력 - 띄어쓰기
            print(graph[i][j], end=' ')
    # 한줄띄우기
    print()