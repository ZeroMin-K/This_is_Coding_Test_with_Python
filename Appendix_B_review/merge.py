# 사전에 정렬된 리스트 a, b
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 a, b의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n+m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길때까지 반복
while i < n or j < m:
    # 리스트B의 모든 원소가 처리되었거나 리스트a의 원소가 더 작을때 
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트a의 원소를 결과 리스트로 이동
        result[k] = a[i]
        i += 1

    # 리스트 a의 모든 원소가 처리되었거나 리스트b의 원소가 더 작을대
    else:
        # 리스트b의 원소를 결과 리스트로 이동
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')