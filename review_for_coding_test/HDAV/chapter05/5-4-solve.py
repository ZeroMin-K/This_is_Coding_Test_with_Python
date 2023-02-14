"""
n * m 크기의 직사각형 형태 미로 - 괴물피해 탈출하기
위치 (1, 1) -> 출구 (n, m)
괴물있으면 0, 없으면 1
미로는 반드시 탈출 
탈출하기 위한 최소 칸의 개수 
시작칸, 마지막칸 모두 포함
"""

# n, m 입력
n, m = map(int, input().split())

#미로 리스트 생성
miro = [] 
# n번 반복하며
for _ in range(n):
    # 미로 입력
    miro.append(list(map(int, input())))

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

# bfs 선언
def bfs():
    # 현재 위치에서 큐 생성
    q = deque()
    # 현재 위치 방문 처리 - 시작 위치는 1이라 나중에 또 방문할 수 있음 => 어쩌피 현재 위치에서 1인부분을 더하는식으로 크게 상관없을듯
    q.append((0, 0))

    print(q)

    #  큐가 빌 때까지 반복
    while q:
        # 다음 위치 좌표 
        x, y = q.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 다음 위치좌표가 유효한 범위이고
            if 0 <= next_x < n and 0 <= next_y < m:
                # 괴물이 없으면 
                if miro[next_x][next_y] == 1:
                    # 현재 위치에서 거리를 더한 값으로 처리 
                    miro[next_x][next_y] = miro[x][y] + 1

                    q.append([next_x, next_y])

#(1, 1)에서 bfs 시작
bfs()


print(miro[n-1][m-1])

