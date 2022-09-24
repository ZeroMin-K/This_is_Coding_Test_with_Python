def sequential_search(n, target, array):
    # 각 원소를 하나식 확인하며
    for i in range(n):
        # 현재 원소가 찾고자 하는 원소와 동일한 경우 
        if array[i] == target:
            return i + 1        # 현재 위치 반환(인덱스는 0부터 시작하므로 1 더함)

input_data = input().split()
n = int(input_data[0])      # 원소 개수 
target = input_data[1]      # 찾고자 하는 문자열

array = input().split()

print(sequential_search(n, target, array))
print(array.count(target))