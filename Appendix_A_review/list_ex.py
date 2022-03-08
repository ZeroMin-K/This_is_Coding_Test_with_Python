array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

n = 3
m = 4
array = [[0]* m for _ in range(n)]
print(array)

a = [1,4,3]
print(a)

a.append(2)
print(a)

a.sort()
print(a)

a.sort(reverse = True)
print(a)

a.reverse()
print(a)

a.insert(2, 3)
print(a)

print(a.count(3))

a.remove(1)
print(a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)