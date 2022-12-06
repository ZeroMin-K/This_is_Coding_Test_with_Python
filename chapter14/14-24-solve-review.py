"""
특정 위치 집에 한개 안테나 설치 
안테나로부터 모든 집까지 거리의 총합이 최소 
동일한 위치 여러개 집 존재 가능
집 위치 정렬 

안테나 설치할 위치 값 출력 - 여러 개 값 도출시 가장 작은 값 출력 
"""

# 집의 수 n 입력
n = int(input())

# n채의 집에 위치가 공백 기준으로 입력
houses = list(map(int, input().split()))

# 집 위치 리스트 정렬 
houses.sort()

# 중앙의 값이 모든 집까지 거리 총합이 짧음. 
loc = len(houses) // 2 - 1
dist_sum = sum([abs(num - houses[loc]) for num in houses])
for next_loc in range(loc, loc + 2):
    next_dist_sum = sum([abs(num - houses[next_loc]) for num in houses])
    if next_dist_sum < dist_sum:
        loc = next_loc 
        dist_sum = next_dist_sum

print(houses[loc])