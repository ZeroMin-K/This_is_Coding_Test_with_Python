array = []
# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) +1)

for i in range(len(array)):
    count[array[i]] += 1        # 각 데이터에 해당하는 인덱스값 증가

for i in range(len(count)):     # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')