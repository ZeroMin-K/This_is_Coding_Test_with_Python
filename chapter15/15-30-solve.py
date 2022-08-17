def solution(words, queries):
    answer = []
    
    # 이진탐색을 통해 매칭되는 것 중 가장 왼쪽 인덱스, 가장 오른쪽인덱스 구해서 개수 파악 가능
    # 파이썬 bisect 이용해서 구함 => bisect는 부분매칭은 어려움
    # ?가 앞에 있을때 words를 뒤집어서 저장하고 다시 정렬해서 진행 
    
    # ?가 앞에 있을 때 접두사 쿼리리스트  prefix_queries
    prefix_queries = []            
    # ?가 뒤에 있을 때 접미사 쿼리리스트  postfix_queries
    postfix_queries = []
    
    # queries 순회
    for query in queries: 
        # ?가 앞에 있을 때 (접두사)
        if query[0] == '?':
            # prefix_queries에 append
            prefix_queries.append(query)
        # ?가 뒤에 있을 때 (접미사)
        if query[-1] == '?':
            # postfix_queries에 append
            postfix_queries.append(query)

    print('접미사 쿼리', prefix_queries)
    print('접두사 쿼리', postfix_queries)
            
    # query에 매칭되는 단어가 몇번 등장하는지 저장할 딕셔너리 query_dict 생성
    query_dict = {}
    
    # ?가 접미사일때 (앞에 부분이 겹칠때의 경우) 부터 찾기
    # words 정렬
    words.sort()
    
    # postfix_queries 순회하면서
    for query in postfix_queries:
        # 현재 query 
        # 앞에 어느 부분까지 문자인지 확인 => 부분 문자 파악 query_part
        pattern_index = 0
        for ch in query:
            if ch != '?':
                pattern_index += 1
        # 부분 쿼리
        query_part = query[:pattern_index]
        
        print('-----------------------------------------------------')
        print('현재 쿼리', query)
        print('부분 쿼리', query_part)
        print('인덱스', pattern_index)
        
        # 이진탐색해서 가장 왼쪽 인덱스 구함
        left_index = bisect_left(words, query, query_part, pattern_index)

        
        print('가장 왼쪽 인덱스', left_index)


        # 가장 오른쪽인덱스 구함
        right_index = bisect_right(words, query, query_part, pattern_index)

        print('가장 오른쪽 인덱스', right_index)
        
        
        # 매칭되는 문자열 개수 오른쪽인덱스 - 왼쪽인덱스 개수 + 1
        match = right_index - left_index + 1
        
        # 매칭되는 문자열이 없으면 
        if left_index == -1:
            match = 0 

        print('개수', match)

        # query_dict에 query와 개수 저장
        query_dict[query] = match 
    
    # ?가 접두사 일때 (뒤에 부분이 겹칠 때의 경우) 부터 찾기 
    # words를 순회하면서
    for i in range(len(words)):
        # words를 반대로 저장
        words[i] = words[i][::-1]
        
    # words sort
    words.sort()

    print('------------------------------------')
    print('words 반대로')
    print(words)
    
    # prefix_queries 순회하면서
    for query in prefix_queries:
        # 현재 query
        # 현재 쿼리 뒤집기
        reverse_query = query[::-1]

        print('현재 쿼리', query)
        print('쿼리 뒤집기', reverse_query)
        
        # 앞에 어느 부분까지 문자인지 확인 => 부분 문자 파악 query_part
        pattern_index = 0
        for ch in reverse_query:
            if ch != '?':
                pattern_index += 1
                
        # 부분 쿼리
        query_part = reverse_query[:pattern_index]

        print('부분 쿼리', query_part)
                
        # 이진 탐색해서 가장 왼쪽 인덱스 구함
        left_index = bisect_left(words, query, query_part, pattern_index)
        # 가장 오른쪽 인덱스 구함
        right_index = bisect_right(words, query, query_part, pattern_index)

        # 매칭되는 문자열 개수 오른쪽인덱스 - 왼쪽인덱스 개수 + 1
        match = right_index - left_index + 1
        
        # 매칭되는 문자열이 없으면 
        if left_index == -1:
            match = 0 

        # query_dict에 query와 개수 저장
        query_dict[query] = match 
    
    # query 순회하면서
    for query in queries:
        # 현재 query랑 query_dict 비교해서 개수 확인
        # 개수를 answer 리스트에 append 
        answer.append(query_dict[query])
        
    return answer

def bisect_left(words, query, target, pattern_index):
    index = -1
    start = 0
    end = len(words) -1 
    
    while start <= end:
        mid = (start + end) // 2
        # word의 pattern index 까지 문자열
        word_part = words[mid][:pattern_index]
        
        if word_part == target:
            if len(words[mid]) == len(query):
                index = mid
                end = mid - 1
            elif len(words[mid]) < len(query):
                start = mid + 1
            else:
                end = mid - 1
        elif word_part < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return index

def bisect_right(words, query, target, pattern_index):
    index = -1
    start = 0
    end = len(words) -1
    
    while start <= end:
        mid = (start + end) // 2
        # word의 pattern index 까지 문자열
        word_part = words[mid][:pattern_index]

        if word_part == target:
            if len(words[mid]) == len(query):
                index = mid
                start = mid + 1
            elif len(words[mid]) < len(query):
                start = mid + 1
            else:
                end = mid - 1
        elif word_part < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return index 

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))