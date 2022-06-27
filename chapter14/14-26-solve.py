n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

# 최소 비교를 위해 정렬 
data.sort()

if n == 1:
    # 묶음이 하나면 비교를 안함. 
    result = 0
else:
    # 최종 섞은 횟수 
    result = 0
    # 이전의 카드 묶음과 비교횟수 - 처음은 첫번째 카드묶음. 
    total = data[0]
    for i in range(1, n):
        # 현재 묶음과 이전 묶음 비교
        total += data[i]

        # 이전의 비교 횟수와 현재 비교횟수 합치기 
        result = result + total

print(result)