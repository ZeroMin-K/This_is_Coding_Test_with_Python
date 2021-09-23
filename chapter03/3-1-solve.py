n = 1260
money_list = [500, 100, 50, 10]

count = 0
rest = n
while rest > 0:
    for money in money_list:
        count += rest // money
        rest = rest % money

print(count)
