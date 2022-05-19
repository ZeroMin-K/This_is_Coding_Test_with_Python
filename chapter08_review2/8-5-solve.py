n, m = map(int, input().split())
coin_type = []

for _ in range(n):
    coin_type.append(int(input()))

dp = [int(1e9)] * (m+1)

for i in range(1, m + 1):
    result = dp[i]
    for coin in coin_type:
        cost = i - coin
        if cost > 0:
            result = min(result, dp[cost] + 1)
        elif cost == 0:
            result = 1

    dp[i] = result
print(dp)

if dp[m] >= int(1e9):
    print(-1)
else:
    print(dp[m])