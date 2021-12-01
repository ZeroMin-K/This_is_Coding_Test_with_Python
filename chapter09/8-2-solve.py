INF = int(1e9)

n, m = map(int, input().split())
array = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a][b] = 1
    array[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            array[i][j] = 0

for d in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            array[i][j] = min(array[i][j], array[i][d] + array[d][j])

distance = array[1][k] + array[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
