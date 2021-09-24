n, m = map(int, input().split())

card_list = []
for _ in range(n):
    sub = list(map(int, input().split()))
    card_list.append(sub)

min_list = []
for card in card_list:
    min_card = min(card) 
    min_list.append(min_card)

print(max(min_list))
