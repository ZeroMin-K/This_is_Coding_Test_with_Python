import time

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

start = time.time()

a.sort()
b.sort(reverse = True)

for i in range(k):
    a[i], b[i] = b[i], a[i]

print(sum(a))

end = time.time()
print(end - start)
