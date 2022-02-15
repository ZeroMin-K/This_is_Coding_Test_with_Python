n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)
while start <= end:
    mid = (start + end) // 2
    dsum = 0
    for height in heights:
        cut = height - mid
        if cut > 0:
            dsum += cut

    if dsum == m:
        result = mid
        break

    if dsum < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)