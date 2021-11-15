n, m = map(int, input().split())
array = []
for _ in range(n):
    line = list(map(int, input().split()))
    array.append(min(line))

print(max(array))
