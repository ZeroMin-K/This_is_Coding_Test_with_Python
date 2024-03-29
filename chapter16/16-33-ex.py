n = int(input())        # 전체 상담 개수
t = []      # 각 상담을 완료하는데 걸리는 시간
p = []      # 각 상담을 완료했을때 받을 수 있는 금액
dp = [0] * (n + 1)          # 1차원 dp테이블 초기화 
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i

    # 상담이 기간안에 끝나는 경우 
    if time <= n:
        # 현재까지 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우 
    else:
        dp[i] = max_value

print(max_value)