loc = input()
col_list = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(col_list)):
    if loc[0] == col_list[i]:
        x = i
y = int(loc[1])

count =0
move_types = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
for move in move_types:
    next_x = x + move[0]
    next_y = y + move[1]
    if 1<= next_x <= 8 and 1 <= next_y <= 8:
        count += 1

print(count)
