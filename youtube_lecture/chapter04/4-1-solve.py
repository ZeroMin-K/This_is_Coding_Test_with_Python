n = int(input())
plan = list(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = 1
y = 1
for step in plan:
    if step == 'L':
        i = 0
    elif step == 'R':
        i = 1
    elif step == 'U':
        i = 2
    elif step == 'D':
        i = 3
    
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    else:
        x = nx
        y = ny

print(x, y)
