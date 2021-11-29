# 정수 n 입력
n = int(input())
# 모든 식량 정보 입력
array = list(map(int, input().split()))

# dp 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행 (바텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

# 계산된 결과 출력
print(d[n-1])
