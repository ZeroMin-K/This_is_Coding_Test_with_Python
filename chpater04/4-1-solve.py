n = int(input())
path_list = list(map(str, input().split()))

x, y = 1, 1

for path in path_list:
    if x == 1 and path == 'U':
        continue
    elif y == 1 and path == 'L':
        continue
    elif x == n and path == 'D':
        continue
    elif y == n and path == 'R':
        continue
    else:
        if path == 'U':
            x -= 1
        elif path == 'R':
            y += 1
        elif path == 'L':
            y -= 1
        elif path == 'D':
            x += 1

print(x, y)
