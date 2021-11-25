n = int(input())
parts_list = list(map(int, input().split()))
parts_list.sort()

m = int(input())
check_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid -1 
        else:
            start = mid + 1

    return False

for check in check_list:
    if binary_search(parts_list, check, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
