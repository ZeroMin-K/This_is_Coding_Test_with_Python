n = int(input())

array = []
for _ in range(n):
    name, score = input().split()
    array.append((int(score), name))

array.sort()
for student in array:
    print(student[1], end= ' ')
