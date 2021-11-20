array = list(input())
zero_count = 0
one_count = 0
prev= array[0]
state = int(array[0])
for elem in array:
    if prev == '0' and elem == '1':
        one_count += 1
        state = 1
    elif prev == '1' and elem == '0':
        zero_count += 1
        state = 1
    prev = elem

if state == 0:
    one_count += 1
else:
    zero_count += 1

print(min(one_count, zero_count))
