n = int(input())

array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, score))

def setting(data):
    return data[1]

array = sorted(array, key=setting)

for data in array:
    print(data[0], end=' ')