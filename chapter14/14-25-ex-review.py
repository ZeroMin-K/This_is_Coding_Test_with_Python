def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러있는 사람 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율 기준으로 각 스테이지 내림차순
    answer = sorted(answer, key = lambda t: t[1], reverse = True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer