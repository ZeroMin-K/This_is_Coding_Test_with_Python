x = int(input())

array = [999] * (x+1)
array[1] = 0
array[2] = 1

for n in range(3, x+1):
    if n % 5 == 0 and n // 5 >= 1:
        array[n] = min(array[n//5], array[n-1]) + 1
    elif n % 3 == 0 and n // 3 >= 1:
        array[n] = min(array[n//3], array[n-1]) + 1
    elif n % 2 == 0 and n // 2 >= 1:
        array[n] = min(array[n//2], array[n-1]) + 1
    else:
        array[n] = array[n-1] + 1

print(array[x])
