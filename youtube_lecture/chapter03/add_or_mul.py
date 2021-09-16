num_list = input()

result = 0
for i in range(0, len(num_list)):
    num = int(num_list[i])
    if result == 0 or num == 0:
        result += num
    else:
        result *= num


print(result)
