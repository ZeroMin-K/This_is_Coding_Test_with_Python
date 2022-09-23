array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:        # 원소가 1개인 경우 
        return              # 종료

    pivot = start           # 첫번째 원소를 피벗으로
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        
        # 엇갈렸다면 (right가 더 작아서 left보다 왼쪽에 있으며 pivot에 있는 값보다 더 작음)
        if left > right: 
            # 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 
        else:
            # 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

        # 분할 이후 왼쪽 부분, 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
    