n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for data in array:
    print(data, end=' ')