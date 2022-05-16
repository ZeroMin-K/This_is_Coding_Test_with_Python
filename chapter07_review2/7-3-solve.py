n, m = map(int, input().split())
h_list = list(map(int, input().split()))

start = 0
end = max(h_list)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for h in h_list:
        if h >= mid:
            result += (h - mid)
    if result < m:
        end = mid - 1
    elif result >= m:
        start = mid + 1
        height =  mid 

print(height)