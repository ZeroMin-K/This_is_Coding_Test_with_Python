import math

m, n = map(int, input().split())
array = [True for i in range(1000001)]      # 처음에 모든 수가 소수인것으로 초기화
array[1] = 0        # 1은 소수가 아님

# 에라토스테네스 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):       # 2부터 n 제곱근까지 모든 수확인
    if array[i] == True:        # i가 소수인 경우(남은 수인 경우 )
        # i를  제외한 i의 모든 배수 제거 
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# m부터 n까지의 모든 소수 출력
for i in range(m, n+1):
    if array[i]:
        print(i)