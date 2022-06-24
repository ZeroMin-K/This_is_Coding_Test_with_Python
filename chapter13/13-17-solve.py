from collections import deque

n, k = map(int, input().split())

vir_array = [[0] * (n+1) for _ in range(n+1)]
vir_loc = [deque([]) for _ in range(k+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    j = 1
    for datum in data:
        vir_array[i][j] = datum
        vir_loc[datum].append((i, j))
        j+= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

s, result_x, result_y = map(int, input().split())

for _ in range(s):
    for i in range(1, k+1):
        if vir_loc[i]:
            x, y = deque.popleft(vir_loc[i])

            for j in range(0, 4):
                next_x = x + dx[j]
                next_y = y + dy[j]

                if 1 <= next_x <= n and 1 <= next_y <= n and vir_array[next_x][next_y] == 0:
                    vir_array[next_x][next_y] = i
                    vir_loc[i].append((next_x, next_y))

print(vir_array[result_x][result_y])