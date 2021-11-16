n = int(input())
plan = list(input().split())

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]
x = 1
y = 1

for data in plan:
    if data == 'L':
        next_x = x + x_list[0]
        next_y = y + y_list[0]
    elif data == 'R':
        next_x = x + x_list[1]
        next_y = y + y_list[1]
    elif data == 'U':
        next_x = x + x_list[2]
        next_y = y + y_list[2]
    else:
        next_x = x + x_list[3]
        next_y = y + y_list[3]
    
    if 1 <= next_x <= n and 1 <= next_y <= n:
        x = next_x
        y = next_y

print(x, y)
