from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

# 각 강의시간 0으로 초기화 
time = [0] * (v+1)

# 방향 그래프 모든 간선정보 입력 
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]       # 첫번째 수는 시간 정보
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상정렬
def topology_sort():
    result = copy.deepcopy(time)     # 알고리즘 수행 결과 담을 리스트 
    q = deque()                      # 큐 기능을 위한 deque라이브러리 사용

    # 처음시작시 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상정렬 수행결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()