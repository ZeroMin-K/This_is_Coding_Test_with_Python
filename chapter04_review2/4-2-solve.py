loc = input()
x = loc[1]
y = ord(loc[0]) - ord('a') + 1
count = 0

move_list = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
for move in move_list:
    next_x = move[0]
    next_y = move[1]
    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        count += 1

print(count)