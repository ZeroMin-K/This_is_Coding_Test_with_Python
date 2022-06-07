n = int(input())
house = list(map(int, input().split()))
house.sort()

result = (100001, house[n-1])
for ant in house:
    sum = 0
    for loc in house:
        sum += abs(ant - loc)
    
    result = min(result, (sum, ant))

print(result[1])