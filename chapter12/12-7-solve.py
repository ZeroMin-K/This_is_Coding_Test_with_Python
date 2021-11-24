array = input()

left_sum = 0
right_sum = 0

for i in range(len(array)//2):
    left_sum += int(array[i])

for j in range(len(array)//2, len(array)):
    right_sum += int(array[j])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
