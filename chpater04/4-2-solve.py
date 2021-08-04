n = int(input())

time_list = list()

for hour in range(n+1):
    for minute in range(60):
        for sec in range(60):
            time = str(hour) + str(minute) + str(sec)
            time_list.append(time)

count = 0 

for time in time_list:
    if '3' in time:
        count += 1

print(count)
