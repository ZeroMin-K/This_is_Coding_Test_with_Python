# 이진탐색 코드 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        if array[mid] == target:
            return mid
        elif  array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인요청한 부품 번호 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')