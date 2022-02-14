n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

i = 0 
j = 0
for _ in range(k):
    if array_a[i] < array_b[j]:
        array_a[i], array_b[j] = array_b[j], array_a[i]
        i += 1
        j += 1
    else:
        break

print(sum(array_a))