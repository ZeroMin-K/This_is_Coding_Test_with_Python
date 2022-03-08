data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만을 담은 리스트 
key_list = data.keys()
# 값 데이터만을 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])


data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a |b)
print(a & b)
print(a-b)

data = set([1, 2, 3])
print(data)

data.add(4)

data.update([5, 6])
print(data)

data.remove(3)
print(data)