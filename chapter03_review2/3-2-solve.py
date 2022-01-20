n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[len(array) - 1]
second = array[len(array) -2]

count = m // (k+1)
rest = m % (k+1)

sum = ((k * first) + second) * count
if rest:
    sum += first * rest

print(sum)