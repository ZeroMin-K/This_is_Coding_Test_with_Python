t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    gold = [[0] * m for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    array = list(map(int, input().split()))
    
    i = 0
    j = 0
    for item in array:
        if j == m:
            j = 0
            i += 1
        gold[i][j] = item
        j += 1
    
    for i in range(n):
        dp[i][0] = gold[i][0]


    for i in range(0, n):
        for j in range(1, m):
            if i-1 >= 0 and i+1 <= n-1:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + gold[i][j]
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + gold[i][j]
            if i == n-1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + gold[i][j]

    max_gold = []
    for i in range(0, n):
        max_gold.append(dp[i][m-1])

    print(max(max_gold))
    print(dp)
