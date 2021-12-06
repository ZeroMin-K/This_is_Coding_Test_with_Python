import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

edges.sort()

cost = 0 
for edge in edges:
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        union_parent(parent, edge[1], edge[2])
        cost += edge[0]

print(cost) 
