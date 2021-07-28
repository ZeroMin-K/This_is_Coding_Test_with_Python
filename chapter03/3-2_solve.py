n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

sum = 0
count = 0

for _ in range(m):
    i = len(num_list) - 1

    if count == k:
        i -= 1
        count = 0

    sum += num_list[i]
    count += 1
    
print(sum)
