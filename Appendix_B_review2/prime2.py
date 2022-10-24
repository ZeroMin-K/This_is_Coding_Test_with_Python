import math
from pickle import FALSE

# 소수 판별함수 
def is_prime_number(x):
    # 2부터 x의 제곱근까지 모든 수 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당수로 나누어떨어진다면
        if x % i == 0:
            return False    # 소수 아님
    return True # 소수

print(is_prime_number(4))