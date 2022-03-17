data = input()

alpha_list = []
sum = 0

for elem in data:
    if ord(elem) - ord('A') >= 0:
        alpha_list.append(elem)
    else:
        sum += int(elem)

alpha_list.sort()

for alpha in alpha_list:
    print(alpha, end='')
print(sum)