import time
n = int(input())

start = time.time()

count = 0
for hour in range(0, n+1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if '3' in str(hour) or '3' in str(minute) or '3' in str(second):
                count += 1

end = time.time()
print(count, end - start)
