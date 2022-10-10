# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0       # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0       # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:      # 쌍이 맞지 않는 경우 
                return False    # False 반환

    return True     # 쌍이 맞는 경우 True 반환

def solution(p):
    answer = ''
    # 빈 문자열일 경우 
    if p == '':
        # 빈 문자열 반환 
        return answer

    # 문자열을 균형잡힌 괄호 문자열 u, v로 분리 
    index = balanced_index(p)       # 균형잡힌 괄호 문자열의 마지막 인덱스 
    u = p[:index + 1]
    v = p[index + 1:]

    # 올바른 괄호 문자열이면 
    if check_proper(u):
        # v에 대해 함수를 수행한 결과를 붙여 반환
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면
    else:
        # 빈 문자열에 첫번째 문자로 ( 붙임
        answer = '('
        # 문자열 v를 과정 수행 후 문자열에 이어 붙임 
        answer += solution(v)
        answer += ')'           

        # 문자열 u의 첫번째, 마지막 문자 제거 
        u = list(u[1:-1])      
        # 문자열을 탐색하며 
        for i in range(len(u)):
            # 문자열의 괄호 방향 뒤집어서 붙이기 
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

    return answer