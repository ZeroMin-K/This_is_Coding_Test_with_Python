from itertools import combinations

l, c = map(int, input().split())
alpha_list = list(input().split())

alpha_list.sort()

for word in list(combinations(alpha_list, l)):
    count = 0
    others = 0
    for alpha in word:
        if alpha in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
        else:
            others += 1
        
    if count >= 1 and others >= 2:
        key = ''.join(list(word))
        print(key)