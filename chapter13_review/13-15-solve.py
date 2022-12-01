"""
1부터 n번까지 도시 , m개의 단방향 도로  모든 도로거리 1
도시 x로부터 출발 모든 도달 도시중 최단거리가 정확히 k인 모든 도시 번호출력
출발도시x에서 출발도시 ㅌ로가는 최단거리 항상0

도시 개수 300,000 => 플로이드 워셜 알고리즘 불가 
BFS로 하나씩 탐색하면서 거리세다가 해당거리에 해당하는 도시들 확인하기 
"""
# 빠른입력
import sys
input = sys.stdin.readline

from collections import deque

# 도시개수 n, 도로 개수 m, 거리정보 k, 출발도시 번호 x입력
n, m, k, x = map(int, input().split())

# 도시 리스트 생성
graph = [[] for _ in range(n + 1)]

# m개의 줄 반복하며
for _ in range(m):
    # a, b 입력 - a번 도시에서 b번 도시로 이동하는 단방향 도로 존재 
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문 테이블 
visited = [False] * (n + 1)

# 거리정보가 k인 리스트
result = []

# bfs
def bfs(visited, start):
    q = deque()             # 큐 생성 
    q.append((start, 0))    # 큐에 시작노드, 현재거리 삽입  
    visited[start] = True   # 시작노드 방문 처리

    while q:        # 큐가 빌 때까지 반복
        # 큐에서 꺼낸 현재 노드, 거리 
        current_node, dist = q.popleft()

        # 현재 거리가 k이면 결과 리스트에 append
        if dist == k:
            result.append(current_node)

        # 현재 노드와 인접한 노드들을 방문하면서 
        for adj_node in graph[current_node]:
            # 방문하지 않은 노드면
            if not visited[adj_node]:
                # 현재거리에 1을 더해서 큐에 삽입
                q.append((adj_node, dist + 1))
                # 방문처리 
                visited[adj_node] = True

# bfs 실행
bfs(visited, x)

result.sort()
if len(result) == 0:    # 도시가 존재하지 않으면 -1 출력
    print(-1)           
else:                   # 도시가 존재하면
    for i in result:    # 하나씩 탐색하며 출력
        print(i)