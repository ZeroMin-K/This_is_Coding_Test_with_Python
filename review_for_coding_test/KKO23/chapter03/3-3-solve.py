"""
가장 높은 숫자가 쓰인 카드 한장 뽑기 
N * M  (행 * 열) 카드 
행 선택해서 가장 숫자가 낮은 카드 뽑아서 최종적으로 가장 큰 숫자 찾기 
각 행을 읽으면서 가장 작은 숫자를 리스트에 넣어서 그 리스트중 가장 큰 수 찾기 
"""

# n, m 입력
n, m = map(int , input().split())

result = []

# n번 반복하며
for _ in range(n):
    # 리스트 읽기
    data = list(map(int, input().split()))
    # 해당 리스트중 가장 작은 숫자 찾아서 결과 리스트에 넣기
    result.append(min(data))

# 결과 리스트 중 가장 큰 숫자 print
print(max(result))