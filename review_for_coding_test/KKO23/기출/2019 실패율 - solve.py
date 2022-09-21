"""
전체 스테이지 수 N, 현재 멈춰있는(도전 중인) 스테이지 번호가 담긴 배열 stages
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수 
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열을 return 

stages를 하나씩 읽으면서 각 스테이지당 클리어 못한 사람 수를 세고
클리어못한 사람 수를 다시 읽으면서 실패율을 확인하며 실패율 리스트를 만듬
실패율 리스트를 실패율로 정렬, 2차로 스테이지로 정렬 
실패율 리스트를 하나씩 확인하며 스테이지 부분만 읽어서 리스트만들어 리턴 
"""

def solution(N, stages):
    answer = []
    
    # N+1 크기의 실패 카운트 리스트 생성 
    fail_counts = [0 for _ in range(N+2)]
    
    # stages를 하나씩 읽으면서 
    for stage in stages: 
        # 실패 카운트 리스트에 해당 스테이지 개수 증가
        fail_counts[stage] += 1

    print(fail_counts)
        
    # 총 인원 = stages의 길이
    total = len(stages)
    # 실패율 리스트 생성
    fail_ratios = []
    
    # 실패 카운트 리스트를 하나씩 읽으며 스테이지 1부터 
    for i in range(1, len(fail_counts) - 1):
        fail_count = fail_counts[i]

        if fail_count == 0:
            fail_ratio = 0
        # 실패율 = 현재 스테이지 실패 사람 수  / 총인원
        else:
            fail_ratio = fail_count / total

        # 실패율 리스트에 (실패율, 스테이지 ) append
        fail_ratios.append((fail_ratio, i))
        
        # 총 인원 = 총인원 - 현재 스테이지 실패 사람 수 
        total -= fail_count

    print(fail_ratios)
        
    # 실패율 리스트 정렬(실패율, 스테이지 순으로 정렬)
    fail_ratios.sort(key = lambda x : (-x[0], x[1]))
    
    
    # 실패율 리스트 하나씩 읽으면서
    for fail_ratio in fail_ratios:
        # 정답 리스트에 스테이지 append
        answer.append(fail_ratio[1])
    
    return answer


print(solution(5, [2,1,2,6,2,4,3,3]))