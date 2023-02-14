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

def dfs(start):
    x = start[0]
    y = start[1]
    graph[x][y] = 1

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]):
            if graph[next_x][next_y] == 0:
                dfs((next_x, next_y))

# 아이스크림 수 
count = 0
# 세로 길이 만큼 인덱스 i 반복
for i in range(len(graph)):
    # 가로 길이 만큼 인덱스 j 반복
    for j in range(len(graph[0])):
        # 현재 위치가 구멍이면
        if graph[i][j] == 0:
            # bfs 진행
            dfs((i, j))
            # bfs 끝나고 나면 아이스크림 수 증가 
            count += 1

for i in range(len(graph)):
    print(graph[i])

# 아이스크림 수 반환
print(count)
