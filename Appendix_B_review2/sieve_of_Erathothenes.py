import math

n = 1000     # 2부터 1000까지 모든 수에대하여 소수 판별
array = [True for i in range(n + 1)]        # 처음에 모든수가 소수(Ture)인 것으로 초기화(0, 1 제외)

# 에라토스테네스의 체 알고르짐 
for i in range(2, int(math.sqrt(n)) + 1):       # 2부터 n의 제곱근까지 모든 수를 확인하며
    if array[i] == True:        # i가 소수인 경우(남은 수인 경우)
        # i 를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')