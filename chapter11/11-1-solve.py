n = int(input())
array = list(map(int, input().split()))

array.sort(reverse = True)

result = 0
count = 0
standard = array[0]

for i in range(n):
    count += 1
    if count == standard:
        result += 1
        j = i + 1
        if j <= n - 1:
            standard = array[j]
            count = 0
        else:
            break

print(result)
