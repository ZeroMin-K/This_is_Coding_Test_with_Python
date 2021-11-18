array = input()
result = int(array[0])
for i in range(1, len(array)):
    now = int(array[i])
    if result == 0 or now == 0 or now == 1:
        result += now
    else:
        result *= now

print(result)
