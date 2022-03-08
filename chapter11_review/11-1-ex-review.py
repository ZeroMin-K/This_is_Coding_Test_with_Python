n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0      # 총 그룹수
count = 0       # 현재 그룹에 포함된 모험가의 수

for i in data:      # 공포도를 낮은것부터 하나씩 확인하며
    count += 1      # 현재 그룹에 해당 모험가 포함
    if count >= i:      # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 결성
        result += 1     # 총 그룹수 증가 
        count = 0       # 현재 그룹에 포함된 모험가 수 초기화

print(result)