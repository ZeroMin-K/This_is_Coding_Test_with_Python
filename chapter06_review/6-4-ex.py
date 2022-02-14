from bdb import Breakpoint


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()                # 배열 a는 오름차순 정렬
b.sort(reverse=True)    # 배열 b는 내림차순 정렬

# 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대K번 비교
for i in range(k):
    # A의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소 교체
        a[i], b[i] = b[i], a[i]
    else:           # a의 원소가 b의 원소보다 크거나 같을 때 반복문 탈출
        break

print(sum(a))