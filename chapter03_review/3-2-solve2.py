n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse = True)

i = 0
sum = 0
for _ in range(m):
    if i == k:
        i = 0
        sum += array[1]
    else:
        i += 1
        sum += array[0]

print(sum)
