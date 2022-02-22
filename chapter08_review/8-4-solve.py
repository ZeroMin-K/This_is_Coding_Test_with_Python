n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    dp[n] = dp[n-1] + dp[n-2] * 2
print(dp[n] % 796796)