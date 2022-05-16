from re import L


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우 
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:   # a의 원소가 b의 원소보다 크거나 같을때 반복문 탈출
        break

print(sum(a))