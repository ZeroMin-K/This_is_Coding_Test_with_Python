def in_chess(x, y):
    if x < 0 or x > 8 or y < 0 or y > 8:
        return False
    else:
        return True

loc = input()
x = loc[0]
y = loc[1]

x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y_list = ['1', '2', '3', '4', '5', '6', '7', '8']
count = 0

i = x_list.index(x)
j = y_list.index(y)


# 왼쪽 위
new_i = i - 2
new_j = j - 1

if in_chess(new_i, new_j):
    count += 1

# 왼쪽 아래  
new_i = i - 2
new_j = j + 1

if in_chess(new_i, new_j):
    count += 1

# 오른쪽 위
new_i = i + 2
new_j = j - 1

if in_chess(new_i, new_j):
    count += 1

# 오른쪽 아래
new_i = i + 2
new_j = j + 1

if in_chess(new_i, new_j):
    count += 1

# 위쪽 왼쪽
new_j = j - 2 
new_i = i - 1

if in_chess(new_i, new_j):
    count += 1

# 위쪽 오른쪽
new_j = j - 2 
new_i = i + 1

if in_chess(new_i, new_j):
    count += 1

# 아래 왼
new_j = j + 2 
new_i = i - 1

if in_chess(new_i, new_j):
    count += 1

# 아래 오른 
new_j = j + 2 
new_i = i + 1

if in_chess(new_i, new_j):
    count += 1

print(count)
