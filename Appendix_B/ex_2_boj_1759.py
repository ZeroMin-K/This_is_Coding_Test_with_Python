import itertools

length, count = map(int, input().split())
word_list = input().split()

word_list.sort()

list_a = ['a', 'e', 'i', 'o', 'u']
alpha_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
list_b = [x for x in alpha_list if x not in list_a]

for word in itertools.combinations(word_list, length):
    a_count = 0
    b_count = 0
    for character in list(word):
        if character in list_a:
            a_count += 1
        if character in list_b:
            b_count += 1
        
    if a_count > 0 and b_count >1:
        word = ''.join(list(word))
        print(word)
