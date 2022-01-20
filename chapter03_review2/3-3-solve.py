n, m = map(int, input().split())

result = 0
for _ in range(n):
    array = list(map(int, input().split()))
    min_num = min(array)
    result = max(result, min_num)

print(result)