array = input()

sum = 0
result = []
for chr in array:
    if chr.isalpha():
        result.append(chr)
    elif chr.isdigit():
        sum += int(chr)

result.sort()
for data in result:
    print(data, end='')
print(sum)
