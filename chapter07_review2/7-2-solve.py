n = int(input())
parts_list = list(map(int, input().split()))

m = int(input())
order_list = list(map(int, input().split()))

parts_list.sort()

def bisearch(key):
    start = 0
    end = len(parts_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if parts_list[mid] == key:
            return True
        elif parts_list[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return False

for order in order_list:
    if bisearch(order):
        print('yes', end=' ')
    else:
        print('no', end=' ')