# 소수 판별 함수
def is_prime_number(x):
    # 2qnxj (x-1)까지 모든 수 확인
    for i in range(2, x):
        #x가 해당수로 나누어 떨어지면
        if x % i == 0:
            return False    # 소수가 아님
    return True     # 소수

print(is_prime_number(4))