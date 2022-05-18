n = int(input())
food_list = list(map(int, input().split()))

for i in range(3, n):
    food_list[i] = max(food_list[i-2] + food_list[i], food_list[i-1])

print(food_list[n-1])