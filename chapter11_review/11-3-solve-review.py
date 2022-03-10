str_data = input()

to_one = 0
to_zero = 0
if str_data[0] == '0':
    zero_state = True
    one_state = False
else:
    zero_state = False
    one_state = True

for data in str_data[1:]:
    if zero_state == True and data == '1':
        zero_state = False
        to_one += 1
    elif data == '0':
        zero_state = True

    if one_state == True and data == '0':
        one_state = False
        to_zero += 1
    elif data == '1':
        one_state = True

if zero_state:
    to_one += 1

if one_state:
    to_zero += 1

print(min(to_zero, to_one))