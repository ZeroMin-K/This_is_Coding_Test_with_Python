n, m = map(int, input().split())
h_list = list(map(int, input().split()))

# 이진 탐색 소스 코드 구현(반복문)
def binary_search(start, end):
    while start <= end:
        mid = (start + end) //2
        
        sum = 0
        for item in h_list:
            item -= mid
            if item > 0:
                sum += item 

        if m == sum:
            return mid
        elif m > sum: 
            end = mid -1
        else:
            start = mid + 1

    return None


# 이진 탐색 수행 결과 출력
result = binary_search(0, max(h_list))
print(result)
