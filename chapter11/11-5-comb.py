from itertools import combinations

n, m = map(int, input().split())
weight = list(map(int, input().split()))

result = 0
for a, b in combinations(weight, 2):
    if a != b:
        result += 1

print(result)
