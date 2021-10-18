from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

right = bisect_right(array, x)
left = bisect_left(array, x)

print(right - left)
