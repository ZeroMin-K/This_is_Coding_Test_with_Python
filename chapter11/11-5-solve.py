n, m = map(int, input().split())
array = list(map(int, input().split()))

count = 0
length = len(array)
for i in range(length -1):
    for j in range(i+1, length):
        if array[i] != array[j]:
            count += 1

print(count)
