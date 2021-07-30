n, k = map(int, input().split())
result = 0

# N이 K이상이면 K로 계속 나누기
while n >= k:
    # N이 k로 나누어 떨어지지 않는다면 n에서 1빼기
    while n % k != 0:
        n -= 1
        result += 1

    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
