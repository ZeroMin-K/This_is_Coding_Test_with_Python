"""
n명의 학생 이름, 국어, 영어, 수학 점수 - 학생 성적 정렬
정렬 조건
1. 국어 점수 감소
2. 국어점수 같으면 영어점수 증가
3. 국어점수, 영어점수 같으면 수학 점수 감소
4. 모든 점수 같으면 이름 사전순으로 증가 
"""

import sys 
input = sys.stdin.readline

# 각 학생들 성적 담는 리스트 생성 
scores = []

# 학생수 n 입력
n = int(input())
# n번 반복하며
for _ in range(n):
    # 한 줄씩 공백기준으로 리스트로 입력 
    data = list(input().split())
    # 학생 이름, 국어, 영어, 수학 점수으로 나누어  성적 리스트에 append
    scores.append((data[0], int(data[1]), int(data[2]), int(data[3])))

# 성적 리스트 조건에 따라 정렬
scores.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

# 성적 리스트 하나씩 반복하며
for student in scores:
    # 학생 이름 출력 
    print(student[0])