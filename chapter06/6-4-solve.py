n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_a.sort()

array_b = list(map(int, input().split()))
array_b.sort(reverse = True)

count = 0
for i in range(n):
    if array_a[i] < array_b[i]:
        array_a[i] = array_b[i]
        count += 1
    else:
        break

    if count >= k:
        break

print(sum(array_a))
