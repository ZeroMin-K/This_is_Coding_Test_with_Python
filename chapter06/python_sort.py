array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array1 = array
result = sorted(array1)
print(result)

array2 = array
array2.sort()
print(array2)

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
