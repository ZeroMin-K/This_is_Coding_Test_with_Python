from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i] = list(map(int, input().split()))

indegree = [0] * (n+1)
for i in range(1, len(graph)): 
    for j in range(1, len(graph[i])-1):
        indegree[graph[i][j]] += 1

result = 0
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result += graph[now][0]
    print(now, result)
    for i in range(1, len(graph[now])-1):
        next_node = graph[now][i] 
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

print(result) 
