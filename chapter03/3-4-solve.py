n, k = map(int, input().split())

count = 0

if n % k == 0:
    while n > 1:
        n /= k 
        count += 1

else:
    n -= 1
    count += 1
    while n % k != 0:
        n -= 1
        count += 1
    
    while n > 1:
        n /= k
        count += 1

print(count)
