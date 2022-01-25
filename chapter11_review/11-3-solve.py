data = input()
one_count = 0
zero_count = 0

continuous = False
for num in data:
    if num == '0':
        if continuous == False:
            continuous = True
    else:
        if continuous:
            continuous = False
            one_count += 1

if continuous:
    one_count += 1

continuous = False
for num in data:
    if num == '1':
        if continuous == False:
            continuous = True
    else:
        if continuous:
            continuous = False
            zero_count += 1

if continuous:
    zero_count += 1

print(min(one_count, zero_count))