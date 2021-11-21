n = int(input())
coin_types = list(map(int, input().split()))
coin_types.sort(reverse = True)

num = 1
while True:
    i = num
    for coin in coin_types:
        if i < coin:
            continue
        else:
            i -= coin

        if i == 0:
            break

    if i == 0:
        num += 1
        continue
    else:
        break

print(num)
