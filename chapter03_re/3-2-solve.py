n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
max = num_list[n - 1]
max_next = num_list[n - 2]

rep = m // (k+1)
rest = m % (k+1)

sum = rep * (k * max + max_next) + rest * max 
print(sum)
