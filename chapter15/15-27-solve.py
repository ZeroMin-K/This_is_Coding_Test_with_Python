from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

right = bisect_right(data, x)
left = bisect_left(data, x)

count = right - left
if count:
    print(count)
else:
    print(-1)  