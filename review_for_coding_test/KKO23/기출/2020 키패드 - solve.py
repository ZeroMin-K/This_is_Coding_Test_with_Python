"""
왼손 엄지, 오른손 엄지만을 이용해 숫자 입력 
맨 처음 왼손 엄지는 *에 위치 , 오른속 엄지손가락은 #에 위치 
엄지손가락 사용 규칙
1. 엄지는 상하좌우 4가지방향으로 이동. 키패드 이동한ㅋ칸은 거로 1
2. 왼쪽 열의 3개 숫자 1, 4, 7 입력시 왼손 엄지 사용
3. 오른쪽 열 3개 숫자 3, 6, 9 입력시 오른손 엄지 사용
4. 가운데 열 4개 숫자 2, 5, 8, 0 
    - 두 엄지 손가락의 현재 키패드 위치에서 더 가까운 엄지 손가락 사용
    - 두 엄지 손가락 거리 같으면 오른손잡이는 오른손, 왼손잡이는 왼손 사용 
hand: 순서대로 누를 번호 담긴 배열
hand: 왼손잡이, 오른손 잡이 
각 번호를 누룬 엄지손이 왼손인지 오른손인지 문자열로 return 

배열 하나씩 탐색하면서 조건에 맞게 구현 
"""

def solution(numbers, hand):
    
    # 키패드 2차원리스트 - 4 * 3 
    # 123       - 1 = (0, 0) / 2 = (0, 1) / 3 = (0, 2)
    # 456       - 4 = (1, 0) / 5 = (1, 1) / 6 = (1, 2)
    # 789       - 7 = (2, 0) / 8 = (2, 1) / 9 = (2, 2)
    # *0#       - * = (3, 0) / 0 = (3, 1) / # = (3, 2)
    answer = []
    
    key_pads = {1 : (0,0), 2 : (0, 1), 3 : (0, 2),
               4 : (1, 0), 5 : (1, 1), 6 : (1, 2), 
               7 : (2, 0), 8 : (2, 1), 9 : (2, 2), 0 : (3, 1)}
    
    # 왼손 엄지 좌표
    left_thumb = [3, 0]
    # 오른손 엄지 좌표 
    right_thumb = [3, 2]
    
    def move_left(number):
        # 왼손 엄지 append
        answer.append('L')
        # 왼손 엄지 위치는 숫자 좌표에 맞게 이동 
        left_thumb[0] = key_pads[number][0]
        left_thumb[1] = key_pads[number][1]
        
    def move_right(number):
        # 오른손 엄지 append
        answer.append('R')
        # 오른손 엄지 위치는 숫자 좌표에 맞게 이동
        right_thumb[0] = key_pads[number][0]
        right_thumb[1] = key_pads[number][1]
            
        
    # numbers 를 하나씩 탐색하며 
    for number in numbers: 
        # 현재 번호가  1, 4, 7 이면 
        if number in [1, 4, 7]:
            # 왼손 엄지 이동
            move_left(number)
            
        # 현재 번호가 3, 6, 9 이면
        elif number in [3, 6, 9]:
            # 오른손 엄지 이동
            move_right(number)
        # 현재 번호가 2, 5, 8, 0 이면
        else:
            # 현재번호좌표로부터 왼손 엄지 위치 거리 
            left_distance = abs(left_thumb[0] - key_pads[number][0]) + \
                            abs(left_thumb[1] - key_pads[number][1])
            # 현재 번호좌표로부터 오른손 엄지 위치 거리
            right_distance = abs(right_thumb[0] - key_pads[number][0]) + \
                            abs(right_thumb[1] - key_pads[number][1])
        
            # 왼손 엄지 거리 오른손 엄지 거리 비교 - 왼손이 짧으면
            if left_distance < right_distance:
                # 왼손 엄지 이동
                move_left(number)
            # 오른손이 짧으면
            elif left_distance > right_distance:
                # 오른손 엄지 이동
                move_right(number)
            # 둘다 같으면
            else: 
                # 왼손잡이면
                if hand == 'left':
                    # 왼손 엄지 이동
                    move_left(number)
                # 오른손 잡이면
                else:
                    # 오른손 엄지 이동 
                    move_right(number)
            
    return ''.join(answer)