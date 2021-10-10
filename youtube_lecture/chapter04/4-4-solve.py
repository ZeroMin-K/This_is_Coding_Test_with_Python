s = input()
str_list = []
sum = 0

for item in s:
    if int(ord(item)) - int(ord('A')) >= 0:
        str_list.append(item)
    else:
        sum += int(item)

str_list.sort()

for s in str_list:
    print(s, end='')
print(sum)
