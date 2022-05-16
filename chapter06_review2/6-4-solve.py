n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

i  = 0
for _ in range(k):
    if b[i] > a[i] and i < n:
        a[i] = b[i]
        i += 1
    else:
        break
        
print(sum(a))