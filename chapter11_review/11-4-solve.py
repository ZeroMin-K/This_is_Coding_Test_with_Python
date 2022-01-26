n = int(input())
coin_types = list(map(int, input().split()))
coin_types.sort()

cost = []
result = 0
cost.append(False)

i = 1
while True:
    for coin in coin_types:
        if i == coin:
            continue
        if i - coin >= 1 and cost[i - coin]:
            cost[i] = True

    if not cost[i]:
        result = i
        break

    i += 1

print(result)