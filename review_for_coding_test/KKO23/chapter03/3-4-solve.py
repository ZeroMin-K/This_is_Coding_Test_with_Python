""" 
N에서 1을 빼거나 N을 K로 나누거나
연산들의 최소 횟수 구하기
최대한 K번으로 나눌 수 있게 진행 
N이 K로 나누어떨어지면 K로 나누고 아니면 1을 빼면서 연산 횟수 세기 
"""

# n, k 입력
n, k = map(int, input().split())

# 연산 횟수 = 0 
count = 0

# n이 1이 될때까지 반복
while n > 1:
    # n이 k로 나누어떨어지면
    if n % k == 0:
        # n을 k로 나누기 
        n = n // k 
    # n이 k로 나누어떨어지지 않으면
    else:
        # n에서 1빼기 
        n -= 1

    # 연산 횟수 1증가
    count += 1

# 연산 횟수 print 
print(count)