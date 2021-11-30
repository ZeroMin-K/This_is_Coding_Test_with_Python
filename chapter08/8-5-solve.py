INF = int(1e9)

n, m = map(int, input().split())

coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

dp = [INF] * (10001)
for coin in coin_types:
    dp[coin] = 1

for i in range(1, m+1):
    if dp[i] != INF:
        continue

    min_count = INF
    for coin in coin_types:
        prev = i - coin
        if 0 <= prev <= m:
            min_count = min(min_count, dp[prev] + 1)
    
    dp[i] = min_count

if dp[m] == INF:
    print(-1)
else: 
    print(dp[m])
