# 주어진 수들을 M번 더하여 가장 큰 수 만들기 
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더할 수 없음
# 값이 가장 크게 되려면 가장 큰수를 k번 만큼더하고 그다음 작은수 한번더하고 
# 다시 가장 큰수를 k번 더하는식으로 진행
# 그래서 k+1만큼 더하는 걸 몇번 반복해서 몇번이 남는지 계산하고 나머지는 가장 큰수를 곱해서 더함 

# n, m, k 입력
n, m , k = map(int, input().split())

# 리스트 입력
data = list(map(int, input().split()))

# 내림차순으로 리스트 정렬 
data.sort(reverse = True)

# 결과 값 = 0
result = 0

# m번에서 (k+1)만큼 나눠서 총 몇번 곱하는지, 나머지가 몇인지 구함
times = m // (k+1)
rest = m % (k+1)

# 최종 결과는 몇번곱 * (k * 가장 큰수 + 그다음 작은수) + 나머지 * 가장 큰 수 
result = times * (k * data[0] + data[1]) + rest * data[0]

# 결과 값 print
print(result)

