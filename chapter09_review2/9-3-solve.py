import heapq

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

INF = int(1e9)
distance = [INF] * (n+1)

distance[c] = 0
h = []
heapq.heappush(h, (0, c))
while h:
    dist, now = heapq.heappop(h)
    
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(h, (cost, i[0]))

count = 0
time = distance[0]
for dist in distance:
    if dist >= INF:
        continue
    else:
        count += 1
        time = max(time, dist)

print(count, time)