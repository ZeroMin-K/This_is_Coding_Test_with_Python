n = int(input())
plan_list = list(input().split())

x = 1
y = 1
move_list = ['L', 'R', 'U', 'D']
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for plan in plan_list:
    for i in range(len(move_list)):
        if plan == move_list[i]:
            next_x = x + dx[i]
            next_y = y + dy[i]

    if 1 <= next_x <= n and 1 <= next_y <= n:
        x = next_x
        y = next_y
    
print(x, y)