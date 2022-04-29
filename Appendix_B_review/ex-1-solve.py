import math

m, n = map(int, input().split())

prime_list = [True] * (n+1)
prime_list[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if prime_list[i] == True:
        j = 2
        while i * j <= n:
            prime_list[i * j] = False
            j += 1

for k in range(m, n +1):
    if prime_list[k] == True:
        print(k)