x = int(input())

dp = [0] * (x+1)

dp[x-1] = 1

for i in range(x-2, 0, -1):

    comp_list = []

    for item in [5*i, 3*i, 2 * i, i + 1]:
        if item <= x:
            comp_list.append(item) 

    dp[i] = min(comp_list) + 1

    comp_list.clear()

print(dp[1])
