n = int(input())

score_list = []

for _ in range(n):
    name, score = input().split()
    score_list.append((int(score), name))
    
score_list.sort()

for score in score_list:
    print(score[1], end=' ')