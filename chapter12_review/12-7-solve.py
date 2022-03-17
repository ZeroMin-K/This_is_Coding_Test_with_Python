data = input()

left_sum = 0
right_sum = 0

for i in range(0, len(data)//2):
    left_sum += int(data[i])
for j in range(len(data) // 2, len(data)):
    right_sum += int(data[j])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')