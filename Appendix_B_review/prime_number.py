import math

from numpy import _FlatIterSelf

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False        # 소수가 아님
    return True     # 소수