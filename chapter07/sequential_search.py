# 순차 탐색 
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1    # 현재 위치 반환(인덱스는 0부터 시작. 1더하기)

print('생성할 원소 개수를 입력후 한칸띄고 찾을 문자열 입력.')
input_data = input().split()
n = int(input_data[0])      # 원소의 개수 
target = input_data[1]      # 찾고자 하는 문자열

print('아서 적은 원소 개수만큼 문자열 입력. 구분은 띄어쓰기 한칸')
array = input().split()

# 순차 탐색 수행결과 출력
print(sequential_search(n, target, array))
