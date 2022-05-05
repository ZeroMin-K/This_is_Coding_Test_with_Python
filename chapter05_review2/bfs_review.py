from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [],
    []
]

visited = [False] * 9

bfs(graph, 1, visited)