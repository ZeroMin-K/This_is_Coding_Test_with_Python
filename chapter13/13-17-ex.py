from collections import deque

n, k = map(int, input().split())

graph = []      # 전체 보드 정보를 담는 리스트
data = []       # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄단위로 입력
    graph.append(list(map(int, input().split())))

    for j in range(n):
        # 해당 위치 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 x, y) 삽입
            data.append((graph[i][j], 0, i, j))
    
# 정렬이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스 퍼져나가는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비우선탐색 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 5초가 지나거나 큐가 빌때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 해당 위치로 이동 가능한 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치면 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])