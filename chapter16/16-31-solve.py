
def check(x, y, n, m):
	if 0 <= x <= n-1 and 0 <= y <= m-1:
		return True
	return False

#테스트케이스 입력
test = int(input())

# 테스트케이스만큼 반복
for _ in range(test):
	# n, m 입력
	n, m = map(int, input().split())

	# 금 위치 리스트로 입력
	gold_location = list(map(int, input().split()))

	# 금광 빈 리스트 생성 
	# gold_mine = [ [] * m for _ in range(n)]
	gold_mine = []

	# dp 빈리스트 nm길이로 생성 
	dp = [ [0] * m for _ in range(n)]


	# # n 행만큼 반복하며
	# for i in range(n):
	# 	# m 열만큼 반복하며
	# 	for j in range(m):
	# 		# 현재 금광리스트는 금위치리스트원소
	# 		gold_mine[i][j] = gold_location[i * m + j]

	index = 0
	for i in range(n):
		gold_mine.append(gold_location[index:index+m])
		index += m
				
	# m번 반복하며 -  열을 하나씩 이동
	for y in range(m):		
		# n번 반복하며 - 각 행 하나씩 확인 
		for x in range(n): 
			# 현재위치 [x][y]

			# 이전열 리스트 생성 
			prev_gold = [] 
			prev_gold.append(0)
			
			# [x-1][y-1], [x][y-1], [x+1][y-1]이 존재하는 좌표이면
			dx = [-1, 0, 1]
			for next in dx:
				if check(x - next, y-1, n, m):
					# 이전열 리스트에 append
					prev_gold.append(dp[x - next][y-1])

			# 현재위치의 최대 금크기 dp[n][m] = 현재위치 금크기 [n][m] + 이전열리스트의 max
			dp[x][y] = gold_mine[x][y] + max(prev_gold)

	# dp[n-1][m열] 에서 최대값 찾기 
	max_gold = 0
	for i in range(n):
		max_gold = max(max_gold, dp[i][m-1])
		

	print(max_gold)