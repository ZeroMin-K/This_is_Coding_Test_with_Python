n = int(input())
adv_list = list(map(int, input().split()))
 
adv_list.sort()
result = 0
count = 0

for adv in adv_list:
    count += 1
    if adv == count:
        result += 1
        count = 0

print(result)