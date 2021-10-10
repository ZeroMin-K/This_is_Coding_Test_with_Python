loc = input()

col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(len(col)):
    if loc[0] == col[i]:
        y = i + 1

x = int(loc[1])

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, -1, 1, -1, 1]

count = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
    
print(count) 
