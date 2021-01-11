# 이것이 취업을 위한 코딩테스트다. with Python

---
## Appendix A

1. 자료형

- 수 자료형: 정수형, 실수형

  - round()함수를 이용 실수형 데이터 비교
  
    - 코딩 테스트 문제에서 실수형 데이터를 비교할 때, 소수점 다섯 번째 자리에서 반올림한 결과가 같으면 정답으로 인정
    
2. 리스트 자료형

- 리스트 인덱싱과 슬라이싱

- 리스트 컴프리헨션 

  - `array = [i for i in range(20) if i % 2 == 1]`
  
  - 2차원 리스트초기화
  
     ```python
     n = 3
     n= 4
     array = [[0] * m for _ in range(n)]
     ```

  - 리스트 관련 메소드: append(), sort(), reverse(), insert(), count(), remove()
  
- 문자열 자료형 

- 튜플 자료형 

- 사전 자료형 

- 집합 자료형 `data = set(리스트)`

  - 집합 자료형 연산: 합집합 |, 교집합 &, 차집합 - 
  
2. 조건문

- 비교/논리 연산자, in/not in 연산자

3. 반복문

- while문

- for문

4. 함수

5. 입출력

- 공백으로 구분한 여러 데이터 입력   `data = list(map(int, input().split()))`

-  빠른 입력

```python
import sys
data = sys.stdin.readline().rstrip()
```

  - 공백문자를 제거하기 위해 rstrip()함수 사용

6. 주요 라이브러리의 문법과 유의점

- 내장함수

  - min(), max(), eval(), sorted(), iterable 객체의 sort()
  
- itertools : 반복되는 데이터를 처리하고 있는 기능을 포함하고 있는 라이브러리

  - permutations: iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)계산
    ```pyton
    from itertools import permutations
    result = listS(permutations(리스트, 뽑을 수))
    ```
    
  - combination: iterable 객체에서 r개의 데이터를 뽑아 순서 고려하지 않고 나열하는 모든 경우(조합) 계산
    ```pyton
    from itertools import combinations
    result = list(combinations(리스트, 뽑을 수))
    ```
    
  - product: iterable객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)계산 - 중복 허용
    ```pyton
    from itertools import product
    result = list(product(리스트, repeat = 뽑을 수))
    ```
  
  - combinations_with_replcement: iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) 계산 - 중복 허용
    ```pyton
    from itertools import combinations_with_replacement
    result = list(combinations_with_replacement(data, 2))
    ```
    
- heapq

  - heap sort 구현 (min heap)
    ```python
    import heapq
    def heapsort(iteralbe):
      h = []
      result = []
      
      for value in iterable:
        heapq.heappush(h, value)
      for i in range(len(h)):
        result.append(heapq.heappop(h))
      return result
    ```

  - max heap heap sort 구현
  
    `heapq.heappush(h, -value)` `result.append(-heapq.heappop(h))` 으로 변경
 
 - bisect: 이진 탐색
 
   - bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 찾기
   
   - bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스 찾기 
   
   - 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할 때 효과적
   
- collections: 자료구조 제공
  
  - deque : 인덱싱, 슬라이싱 불가
    
    - popleft(): 첫번째 원소 제거, appendleft(): 첫번째 인덱스에 원소 삽
  
  - Counter: iterable객체가 주어졌을 때 해당 객체 내부의 원소가 몇번씩 등장했는지 알려줌

- math 
  
  - factorial(), sqrt(), gcd(), pi, e

