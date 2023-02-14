"""
n * m 크기 얼음틀 - 구멍 0, 칸만이 1
구멍 상, 하, 좌, 우 붙으면 서로 연결
생성되는 아이스크림 개수 
"""

# 세로 길이 n, 가로길이 m 입력
n, m = map(int, input().split())

graph = []
# n번 반복하며 얼음틀 입력
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(len(graph)):
    print(graph[i])

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
# bfs 선언
def bfs(start):
    # 현재 위치로부터 큐 생성
    q = deque([start])
    # 현재 위치 방문처리
    graph[start[0]][start[1]] = 1

    # 큐가 빌 때까지 
    while q:
        # 큐에서 현재 위치 꺼냄
        x, y = q.popleft()

        # 상, 하, 좌, 우 반복하면서
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 다음 위치가 범위안에 있으면
            if 0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]):
                # 다음위치가 0이면
                if graph[next_x][next_y] == 0:
                    # 방문처리
                    graph[next_x][next_y] = 1
                    # 큐에 넣기
                    q.append((next_x, next_y))

# 아이스크림 수 
count = 0
# 세로 길이 만큼 인덱스 i 반복
for i in range(len(graph)):
    # 가로 길이 만큼 인덱스 j 반복
    for j in range(len(graph[0])):
        # 현재 위치가 구멍이면
        if graph[i][j] == 0:
            # bfs 진행
            bfs((i, j))
            # bfs 끝나고 나면 아이스크림 수 증가 
            count += 1

for i in range(len(graph)):
    print(graph[i])

# 아이스크림 수 반환
print(count)
