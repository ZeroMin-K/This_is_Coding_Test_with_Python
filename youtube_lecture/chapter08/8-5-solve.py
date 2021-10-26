n = int(input())
array = list(map(int, input().split()))

count = 0
for i in range(len(array)-1):
    if array[i] > array[i+1]:
        count += 1

count += 1
print(len(array) - count)
