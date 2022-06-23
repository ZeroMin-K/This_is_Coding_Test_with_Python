#  실패율 - 스테이지도달 but not clear 플레이어 수 / 스테이지 도달 플레이어수 
# 전체 스테이지개수N, 현재 멈춘 스테이지번호 배열 stages
# return 실패율이 높은 스테이지부터 내림차순 배열 return 
# stages에서 현재 값은 도전중인 스테이지. -1 값은 클리어한 스테이지 
# stages를 하나씩 확인해서 각 stage에 해당하는 사람들이 몇명인지 세어 클리어하지 못한 total_stage에 기록
# 실패율 리스트 만들기 
# total_stage를 하나씩 확인하면서 
    # 실패율 계산 - 현재 스테이지 클리어 못한 수 / 총 참여자 계산
    # 실패율 리스트에 실패율과 stage append
# 첫번째 스테이지 총 참여자는 stages 길이만큼이고
# total_stage를 하나씩 확인하면서 총 참여자는 이전 스테이지 클리어못한수에서 빼기 
# 실패율 리스트를 실패율 순으로 정렬해서 
# 실패율 리스트를 앞에서부터 반복하며 
    # answer리스트에 스테이지만 append
    
def solution(N, stages):
    answer = []
    
    # total_stage 리스트 생성 (스테이지 길이 + 2)의 길이 
    # (n번 인덱스는 n번째 스테이지 못한사람, n+1번 인덱스는 n번째 스테이지 합격한 사람 )
    # (따라서 n+2의 길이 필요 => stages값에서 n+1값이 나와도 처리 가능 )
    total_stage = [0] * (N+2) 
    
    # 실패율 리스트 fail_list 생성
    fail_list = []
    
    # stages를 하나씩 확인하면서
    for stage in stages:
        # stage에 맞게 total_stage에 1씩 증가 
        total_stage[stage] += 1
        
    # 총 참여자 total_user = stages 길이 
    total_user = len(stages)
    
    # total_stage를 하나씩 확인하면서
    for i in range(1, N+1):
        # 도달한 유저가 없으면 실패율 0 
        fail = 0
        
        if total_stage[i]: 
            # 실패율 계산 = 현재 값 / 총 참여자 total_user
            fail = total_stage[i] / total_user

        # 실패율 리스트 fail_list에 (실패율, 스테이지) append
        fail_list.append((fail, i))
        
        # 총 참여자 total_user -= 현재값 
        total_user -= total_stage[i]
    
    # fail_list 내림차순 정렬 
    fail_list.sort(reverse = True, key = lambda x: (x[0], - x[1]))
    
    # fail_list 앞에서부터 반복하면서
    for fail in fail_list:
        # answer에 원소[1] (스테이지) append
        answer.append(fail[1])
    
    return answer