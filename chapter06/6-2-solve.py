import sys

n = int(sys.stdin.readline().rstrip())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort(reverse=True)
for num in array:
    print(num, end=' ')
