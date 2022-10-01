"""
현재위치에서 최대는 왼쪽 대각선위에서 오는거, 오른쪽 대각선위에서 오는 것 중 큰거를 더함
오른쪽 대각선위 - 현재위치에서 -1한 행, 같은 열
왼쪽 대각선 위 - 현재위치에서  -1한 행, -1한 열 
왼쪽 대각선위와 오른쪽 대각선위가 인덱스를 벗어나지 않은지 확인 필요 
마지막줄에서 가장 최대값 찾아서 출력
왼쪽 대각선 위에서 오는 경우
    - 현재 열이 0이 아닌 경우 
오른쪽 대각선 위에서 오는 경우 
    - 현재 행과 현재 열이 같지않을 경우(이때는 정사각형) 

"""

# 삼각형의 크기 n 입력
n = int(input())

triangle = []
# n번 반복하며
for _ in range(n):
    # 삼각형 한줄 씩 입력 
    triangle.append(list(map(int, input().split())))

# 다이나믹 프로그래밍 진행
# 삼각형 한 줄 씩 탐색하며
for i in range(n):
    # 삼각형 한줄의 하나씩 탐색하며 
    for j in range(len(triangle[i])):
        left = 0
        right = 0
        # 왼쪽 대각선 에서 오는 경우 
        # 현재 열이 0이 아닌 경우 
        if j != 0:
            # 왼쪽 대각선에서 오는 값 
            left = triangle[i-1][j-1]

        # 오른쪽 대각선위에서 오는 경우 
        # 현재 행과 현재 열이 같지 않을 경우 
        if i != j:
            # 오른쪽 대각선에서 오는 값 
            right = triangle[i-1][j]
        # 둘 중 큰값이 현재 값
        triangle[i][j] = max(left, right) + triangle[i][j]


# 삼각형 마지막 줄에서 최댓값 찾아서 출력
print(max(triangle[n-1]))