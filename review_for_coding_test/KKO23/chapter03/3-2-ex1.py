# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort()     # 정렬
first = data[n-1]       # 가장 큰수 
second = data[n-2]      # 두번째로 큰수 

result = 0

while True:
    for i in range(k):          # 가장 큰수  k번 더하기
        if m == 0:              # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1                  # 더할때 마다 1씩 빼기
    if m == 0:                  # m이 0이라면 반복문 탈출
        break
    result += second            # 두번째로 큰수 한번 더하기
    m -= 1                      # 더할 때마다 1씩 빼기

print(result)