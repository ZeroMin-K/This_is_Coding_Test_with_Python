n = input()
length = len(n)     # 정수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽부분, 오른쪽 부분의 자릿수 합이 동일하닞 검사
if summary == 0:
    print('LUCKY')
else:
    print('READY')