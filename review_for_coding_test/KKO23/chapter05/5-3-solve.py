"""
n * m 크기의 얼음틀  
0 - 구멍 뚫려있는 부분, 1 - 칸막이가 존재하는 부분
구멍이 뚫려있는 부분끼리 서로 연결
얼음 틀의 모양이 주어졌을 때 아이스크림 개수 구하기 

2차원 리스트의 얼음틀을 하나씩 순회하면서 BFS를 진행
BFS를 진행하면서 방문했는지 안했는지 기록
BFS가 끝나면 얼음 수 증가
다음 원소로 진행하는데 방문했으면 넘어가기 
"""
from collections import deque

# 얼음틀 세로길이 n, 가로길이 m 입력
n, m = map(int, input().split())

tray = []
# n번 반복하며 
for _ in range(n):
    # 얼음틀 리스트 입력 
    tray.append(list(input()))

# BFS 정의 : 시작하는 x좌표, 시작하는 y좌표, 얼음틀
def bfs(x, y):

    # 현재 좌표부터 진행하는 큐 생성
    queue = deque([(x, y)])

    # 현재 좌표 방문처리
    tray[x][y] = 1

    # 상, 하, 좌, 우 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 원소 하나 빼기
        now = queue.popleft()

        now_x = now[0]
        now_y = now[1]

        # 현재 좌표와 인접한 좌표들중에서
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if 0 <= next_x <= n-1 and 0 <= next_y <= m - 1:
                # 방문하지 않은 좌표가 있으면
                if tray[next_x][next_y] == 0:
                    # 큐에 삽입
                    queue.append((next_x, next_y))
                    # 방문 처리 
                    tray[next_x][next_y] = 1

# 아이스크림 개수 count - 0으로 초기화 
count = 0

# 얼음틀 리스트 하나씩 반복하며 [i][j]로 하나씩 반복
# i 행 - 0부터 n-1까지 반복
for i in range(n):
    # j 열 - 0부터 m-1까지 반복 
    for j in range(m):
        # 현재 얼음 틀을 방문하지 않았으면 
        if tray[i][j] == 0:
            # 현재 얼음 구멍 위치에서 부터 BFS시작
            bfs(i, j)

            # BFS가 다 종료되면 아이스크림 개수 증가
            count += 1


# 아이스크림 개수 출력
print(count) 