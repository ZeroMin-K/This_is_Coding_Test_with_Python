n = int(input())
array = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[0] = array[0]
dp[1] = array[1]
dp[2] = array[0] + array[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2], dp[i-3]) + array[i]

print(max(dp))
