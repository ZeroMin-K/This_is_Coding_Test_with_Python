# 한번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 저모하식에 따라서 피보나치 결괍 나환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))