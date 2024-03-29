# 데이터 개수 n과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합계산(세번째 수부터 네번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])