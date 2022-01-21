n, k = map(int, input().split())
count = 0

while not (n == 1):
    if n % k == 0:
        n //= k 
    else:
        n -= 1
    count += 1

print(count)