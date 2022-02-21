n = int(input())
array = list(map(int, input().split()))

for i in range(2, n):
    array[i] = max(array[i-2] + array[i], array[i-1])

print(array[n-1])