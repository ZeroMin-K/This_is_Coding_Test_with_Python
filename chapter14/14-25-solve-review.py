"""
실패율 = 스테이지 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어수 
N : 전체 스테이지 개수 (1 <= N <= 500 : 자연수)
stages : 사용자가 멈춰있는 스테이지 번호 담긴 배열 (1 <= 길이 <= 200,000)
    - 1이상 N + 1 이하의 자연수 =>  현재 도전중인 스테이지 번호 
    - N + 1 = 마지막 스테이지 N번까지 클리어한 사용자 
    - 실패율이 같으면 작은 번호 스테이지가 먼저 
    - 스테이지 도달한 유저 없으면 실패율 0 
    - stages 길이 = 사용자 수 
return - 실패율이 높은 스테이지부터 내림차순으로 스테이지번호 담긴 배열 
"""

def solution(N, stages):    
    # 성공하지 못한 사람들의 스테이지 리스트 ( 인덱스 - 스테이지), N+1은 N번째까지 전부 클리어
    failed_stages = [0] * (N + 2)
    
    # stages를 하나씩 읽으면서 
    for stage in stages:
        # 현재 도전중인 사람들을 성공못한 리스트에 추가하기
        failed_stages[stage] += 1
        
    print(failed_stages)
    
    # 스테이지와 실패율을 담는 리스트 생성
    failed_ratios = []
    # 총 사람 수
    people = len(stages)
    # 스테이지 실패 리스트를 하나씩 읽으며
    for i in range(1, N + 1):
        # 현재 스테이지 실패한 사람 수 
        now_failed = failed_stages[i]
        
        if people <= 0:
            failed_ratio = 0
        else:
            # 현재 실패 율
            failed_ratio = failed_stages[i] / people 
        # 현재 실패율, 스테이지 담기 
        failed_ratios.append((failed_ratio, i))
        # 다음 스테이지 사람 수 갱신
        people -= failed_stages[i]
    
    print(failed_ratios)
    
    # 실패율 내림차순, 스테이지 오름차순으로 정렬 
    failed_ratios.sort(key = lambda x: (-x[0], x[1]))
    
    print(failed_ratios)
    
    # 결과 리스트 
    answer = []
    # 정렬된 실패율 리스트를 하나씩읽으며
    for i in range(len(failed_ratios)):
        # 스테이지번호 append
        answer.append(failed_ratios[i][1])
    
    return answer