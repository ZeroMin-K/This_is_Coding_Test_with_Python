n = int(input())
count = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            for time in [str(hour), str(minute), str(second)]:
                if '3' in time:
                    count += 1
                    break

print(count)