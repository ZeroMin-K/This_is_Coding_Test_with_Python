from collections import deque
import sys
input = sys.stdin.readline

# 도시 개수, 도로 개수, 거리 정보 출발도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0     # 출발도시까지 거리 0 으로 설정

# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 됫에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리 k인 모든 도시 번호 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단거리가 k인 도시가 없다면 -1 출력
if check == False:
    print(-1)