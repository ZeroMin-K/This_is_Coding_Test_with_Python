"""
1번부터 n번까지 도시 - M개의 단방향 도로 - 모든 도로 거리1 
특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중 최단거리가 정확히 k인 모든 도시들의 번호 출력
출발도시 x에서  출발도시 x로 가는 최단 거리 항상 0 

x로부터 출발하여 도달할 수 있는 도시 중 최단거리가K인 모든 도시 번호 한줄에 하나씩 오름차순으로 출력
도달할 수 있는 도시 중 최단거리가 K인 도시가 하나도 존재하지 않으면 -1 출력

"""

from collections import deque
import sys

input = sys.stdin.readline

# 도시 개수 n, 도로 개수 m, 거리 정보 k, 출발 도시 번호 x
n, m, k, x = map(int, input().split())

# 도시 그래프 리스트 생성 - 리스트를 원소로 가지는 n+1개의 리스트
graph = [[] for _ in range(n+1)]

# m번 반복하며
for _ in range(m):
    # a, b 입력
    a, b = map(int, input().split())
    # a번 도시에서 b번 도시로 - 인덱스a에 b append
    graph[a].append(b)

# 최단 거리 도시 리스트 생성 
shortest_cities = []

# bfs 함수 정의
def bfs(start, visited):
    # 큐 생성
    q = deque()
    # 현재 도시와 거리를 큐에 삽입
    q.append((start, 0))
    # 현재 도시 방문처리
    visited[start] = True

    # 큐가 빌때까지 반복
    while q: 
        # 큐에서 도시 하나 deque
        now_city, dist = q.popleft()

        # 큐에서 꺼낸 도시의 거리가 k이면
        if dist == k:
            # 최단거리 도시 리스트에 삽입 
            shortest_cities.append(now_city)

        # 도시랑 연결된 도시들중에서
        for city in graph[now_city]:
            # 방문 안한게 있으면
            if visited[city] == False:
                # 방문표시 
                visited[city] = True
                # 거리 증가시켜서 큐에 삽입
                q.append((city, dist + 1))

visited = [False] * (n + 1)

# 도시 x부터 bfs 진행
bfs(x, visited)

# 최단거리 도시 리스트에 아무것도 없으면
if len(shortest_cities) == 0:
    # -1 출력
    print(-1)
# 최단 거리 도시리스트 도시가 있으면
else: 
    # 최단 거리 도시 리스트 정렬
    shortest_cities.sort()
    # 앞에서부터 하나씩 한줄 출력 
    for city in shortest_cities:
        print(city)
