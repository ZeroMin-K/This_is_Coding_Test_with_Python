data = input()
result = int(data[0])

for i in data[1:]:
    i = int(i)
    if result == 0 or i == 0 or i == 1:
        result += i
    else:
        result *= i

print(result)