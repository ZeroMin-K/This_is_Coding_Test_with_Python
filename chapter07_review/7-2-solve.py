def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

n = int(input())
parts = list(map(int, input().split()))

m = int(input())
requests = list(map(int, input().split()))

parts.sort()

for request in requests:
    result = binary_search(parts, request, 0, len(parts) - 1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')