n, m = map(int, input().split())
array = list(map(int, input().split()))

max_height = max(array)

start = 0
end = max_height

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in array:
        rest = i - mid
        if rest >= 0:
            sum += rest
    if sum == m:
        break
    elif sum > m:
        start = mid + 1
    else:
        end = mid - 1

print(mid)
