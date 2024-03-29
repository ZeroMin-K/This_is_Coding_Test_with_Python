import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)      # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[]for i in range(n + 1)]
# 최단 거리테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 경로 0 설정. 큐에 삽입 
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정ㄴ보 꺼내기
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 10):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        print("INIFINTIY")
    # 도달할 수 있는 경우 거리출ㄺ
    else:
        print(distance[i])

        

