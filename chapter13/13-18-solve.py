from collections import deque

# 균형잡힌 괄호 문자열 - (, )의 개수가 같음
# 올바른 괄호 문자열 - (, )의 개수도 맞고 짝도 맞을 경우 

# 균형잡힌 괄호 문자열인지 체크 함수
def is_balanced(before):
    left = 0
    right = 0
    for word in before:
        if word == ')':
            right += 1
        else:
            left += 1
            
    if left == right:
        return True
    else:
        return False
    

# 올바른 괄호 문자열인지 체크 함수
def is_correct(arr):
    # 빈 리스트로 deque 생성
    stack = deque([])
    # 문자열을 하나씩 읽으면서
    for word in arr:
        if word == '(':
            stack.append(word)
        # deque not empty and )를 만나면 
        elif deque and word == ')': 
            stack.pop()



    # deque가 비어있지 않으면
    if stack:
        # 올바른 괄호 문자열 아님
        return False
    # deque가 비어있으면
    else:   
        # 올바른 괄호 문자열 
        return True

    
# 균형잡인 괄호 문자열을 올바른 괄호 문자열로 변환 
# 균형잡힌 문자열이 매개변수 
def make_correct(balanced):
    after = []
    
    # 1. 입력이 빈 문자열 => 빈문자열 반환
    if not balanced:
        return after
    
    # 2. 두 균형잡힌 괄고 문자열 u, v로 분리
        # u는 균형잡힌괄호문자열로 더이상 분리 못함.
        # v는 빈 문자열이 될 수 있음
    u = []
    v = []
    left = 0
    right = 0
    index = 0
    for i in range(0, len(balanced)):
        if balanced[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            index = i + 1
            break

        u.append(balanced[i])

    for j in range(index, len(balanced)):
        v.append(balanced[j])
    
    
    # 3. 문자열 u가 올바른 괄호 문자열이면 v를 1단계부터 다시 수행
    if is_correct(u):
        v = make_correct(v)
    
    # 4. 문자열 u가 올바른 괄호 문자열이 아니면 과정 수행
    else:
        # 4-1. 빈 문자열에 첫번째 문자로 ( 붙임
        after.append('(')
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어붙임
        after.append(v)
        # 4-3. ) 를 다시 붙임
        after.append(')')
        # 4-4. u의 첫번째와 마지막 문제를 제거, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        u = u[1:-1]
        for i in range(0, len(u)):
            if u[i] == ')':
                   u[i] = '('
            else:
                u[i]= ')'
        after += u         
        
    # 4-5. 생성된 문자열 반환
    return after
    
 
def solution(p):
    answer = ''
                   
    if is_correct(p):
        return p
                   
    result = make_correct(p)
                   
    answer = ''.join(result)    
                   
    return answer