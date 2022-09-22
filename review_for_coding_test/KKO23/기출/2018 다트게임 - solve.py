"""
다트게임 총 3번  - 각 기회마다 0점에서 10점 얻음
Single(S) 1제곱, Double(D) 2제곱, Triple(T) 3제곱 점수 계산 영역 
    - 점수마다 하나씩 존재 
스타상 * : 해당 점수와 바로 전에 얻은 점수 2배
    - 첫번째에서도 나올 수 있음. 첫번째 스타상의 점수만 2배 
    - 다른 스타상 효과와 중첩 가능. 
    - 아차상 효과와 중첩 가능 -2배 
아차상 # : 해당 점수 마이너스
두 개 상은 점수마다 둘 중 하나만 존재 or 아예 존재 안함
총점수 반환

문자열 읽으며 조건에 맞게 구현 
"""
def solution(dartResult):
    answer = 0
    
    # 점수에서 10을 다른 문자로 변경 
    dartResult = dartResult.replace("10", "A")
    
    # S, D, T 인덱스 1, 2, 3에 맞게 리스트 초기화 
    bonuses = [' ', 'S', 'D', 'T']
        
    # 다트게임 총 3번 점수 기록하는 리스트 (0번 인덱스 처리하기 위해 길이4)
    dart_games = [0 for _ in range(4)]    
        
    game = 0 
    # 점수 결과를 하나씩 확인하며 
    for i in range(len(dartResult)):
        
        # 현재 문자가 숫자이면
        if dartResult[i].isdigit():
            game += 1
            # 현재 다트게임의 점수는 현재문자 숫자 
            dart_games[game] = int(dartResult[i])
            
        elif dartResult[i] == 'A':
            game += 1
            # 현재 다트게임의 점수는 10
            dart_games[game] = 10
            
        # S, D, T 중 하나면
        elif dartResult[i] in bonuses: 
            # S, D, T 값에 맞는 인덱스 찾아서 
            bonus = bonuses.index(dartResult[i])
            # 현재 게임 점수 보너스 만큼 제곱하기 
            dart_games[game] = dart_games[game] ** bonus
            
        # *이면
        elif dartResult[i] == '*':
            # 이전 게임점수 2배
            dart_games[game - 1] = 2 * dart_games[game - 1]
            # 현재 게임 점수 2배 
            dart_games[game] = 2 * dart_games[game]
            
        # #이면 
        elif dartResult[i] == '#':
            # 현재 점수 -1 배 
            dart_games[game] = (-1) * dart_games[game]
            
            
    # 다트게임 점수 기록 리스트 sum해서 return 
    return sum(dart_games)