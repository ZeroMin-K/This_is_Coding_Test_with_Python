INF = int(1e9)

n, m = map(int, input().split())

dp = [INF] * (100001)
coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

for coin in coin_types:
    dp[coin] = 1

for i in range(1, m+1):
    min_list = []
    for coin in coin_types:
        if i - coin >= 0 and dp[i-coin] != INF:
            min_list.append(dp[i - coin])
    if min_list:
        dp[i] = min(min_list) + 1

if dp[m] == INF:
    dp[m] = -1
print(dp[m])