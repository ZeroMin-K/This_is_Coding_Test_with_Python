import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m , c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

result = 0
result_list = []
for dist in distance:
    if dist != 0 and dist != INF:
        result += 1
        result_list.append(dist)

print(result, max(result_list))