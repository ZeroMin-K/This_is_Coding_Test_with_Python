from tkinter import N


def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = []

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

dfs(graph, 1, visited)