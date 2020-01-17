# [Programmers - 자릿수 더하기](https://programmers.co.kr/learn/courses/30/lessons/12931)

```python

def solution(n):
    answer = 0
    
    lst = [int(i) for i in str(n)]
    
    for i in range(len(lst)):
        
        answer += lst[i]
    
    return answer

# 테스트 1 〉	통과 (0.07ms, 10.8MB)
# 테스트 2 〉	통과 (0.07ms, 10.9MB)
# 테스트 3 〉	통과 (0.08ms, 10.9MB)
# 테스트 4 〉	통과 (0.07ms, 10.8MB)
# 테스트 5 〉	통과 (0.06ms, 11MB)
# 테스트 6 〉	통과 (0.07ms, 10.8MB)
# 테스트 7 〉	통과 (0.06ms, 11MB)
# 테스트 8 〉	통과 (0.07ms, 10.8MB)
# 테스트 9 〉	통과 (0.06ms, 10.8MB)
# 테스트 10 〉	통과 (0.07ms, 10.8MB)
# 테스트 11 〉	통과 (0.06ms, 10.9MB)
# 테스트 12 〉	통과 (0.06ms, 10.9MB)
# 테스트 13 〉	통과 (0.07ms, 10.9MB)
# 테스트 14 〉	통과 (0.07ms, 10.9MB)
# 테스트 15 〉	통과 (0.07ms, 11MB)
# 테스트 16 〉	통과 (0.07ms, 10.9MB)
# 테스트 17 〉	통과 (0.07ms, 10.9MB)
# 테스트 18 〉	통과 (0.07ms, 10.9MB)
# 테스트 19 〉	통과 (0.08ms, 10.8MB)
# 테스트 20 〉	통과 (0.07ms, 10.9MB)
# 테스트 21 〉	통과 (0.06ms, 10.8MB)

```

# [Programmers - 모의고사](https://programmers.co.kr/learn/courses/30/lessons/42840)

```python

def solution(answers):
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    
    count1=0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == stu1[i%5]:
            count1 += 1
        
        if answers[i] == stu2[i%8]:
            count2 += 1
        
        if answers[i] == stu3[i%10]:
            count3 += 1
                
    maxV = max(count1, count2, count3)
    
    answer = []

    if maxV == count1:
       print(answer.append(1))
    if maxV == count2:
        print(answer.append(2))
    if maxV == count3:  
        print(answer.append(3))
    return answer
    
# 테스트 1 〉	통과 (0.05ms, 10.8MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.05ms, 10.8MB)
# 테스트 4 〉	통과 (0.05ms, 10.8MB)
# 테스트 5 〉	통과 (0.05ms, 10.7MB)
# 테스트 6 〉	통과 (0.06ms, 10.7MB)
# 테스트 7 〉	통과 (1.15ms, 11.1MB)
# 테스트 8 〉	통과 (0.43ms, 11MB)
# 테스트 9 〉	통과 (2.24ms, 13.7MB)
# 테스트 10 〉	통과 (1.06ms, 11.1MB)
# 테스트 11 〉	통과 (2.38ms, 14MB)
# 테스트 12 〉	통과 (1.99ms, 13.4MB)
# 테스트 13 〉	통과 (0.16ms, 10.8MB)
# 테스트 14 〉	통과 (2.35ms, 14.6MB)

```

# [programmers - 콜라츠 추측] (https://programmers.co.kr/learn/courses/30/lessons/12943)

```python
def solution(n):
    answer = 0

    for answer in range(500):
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 +1
        if n == 1:
            return answer + 1
    return -1

# testcase 13 실패

def solution(n):
    answer = 0
    for answer in range(500):
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        if n == 1:
            return answer + 1
    return -1
    
# testcase 13 실패

# 테스트 1 〉	통과 (0.07ms, 10.8MB)
# 테스트 2 〉	통과 (0.08ms, 10.7MB)
# 테스트 3 〉	통과 (0.08ms, 10.7MB)
# 테스트 4 〉	통과 (0.06ms, 10.6MB)
# 테스트 5 〉	통과 (0.15ms, 10.7MB)
# 테스트 6 〉	통과 (0.07ms, 10.7MB)
# 테스트 7 〉	통과 (0.16ms, 10.7MB)
# 테스트 8 〉	통과 (0.06ms, 10.7MB)
# 테스트 9 〉	통과 (0.06ms, 10.7MB)
# 테스트 10 〉	통과 (0.16ms, 10.6MB)
# 테스트 11 〉	통과 (0.14ms, 10.7MB)
# 테스트 12 〉	통과 (0.06ms, 10.7MB)
# 테스트 13 〉	실패 (0.18ms, 10.7MB)
# 테스트 14 〉	통과 (0.07ms, 10.7MB)
# 테스트 15 〉	통과 (0.06ms, 10.7MB)
# 테스트 16 〉	통과 (0.07ms, 10.7MB)

def solution(n):
    answer = 0
    # i = 0
    while n > 1:
        n = n * 3 + 1 if n % 2  else n / 2
        answer += 1
    return answer if answer < 500 else -1


# 테스트 1 〉	통과 (0.07ms, 10.7MB)
# 테스트 2 〉	통과 (0.08ms, 10.7MB)
# 테스트 3 〉	통과 (0.09ms, 10.7MB)
# 테스트 4 〉	통과 (0.06ms, 10.7MB)
# 테스트 5 〉	통과 (0.15ms, 10.6MB)
# 테스트 6 〉	통과 (0.07ms, 10.7MB)
# 테스트 7 〉	통과 (0.15ms, 10.8MB)
# 테스트 8 〉	통과 (0.07ms, 10.8MB)
# 테스트 9 〉	통과 (0.06ms, 10.7MB)
# 테스트 10 〉	통과 (0.15ms, 10.7MB)
# 테스트 11 〉	통과 (0.16ms, 10.7MB)
# 테스트 12 〉	통과 (0.07ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.8MB)
# 테스트 14 〉	통과 (0.07ms, 10.7MB)
# 테스트 15 〉	통과 (0.07ms, 10.6MB)
# 테스트 16 〉	통과 (0.07ms, 10.7MB)

```

```pyhton

삼항 연산자 (Tenary operators)

참인 경우 값 if 조건 else 거짓인 경우 값


```

# [Programmers - 완주하지 못한 선수] (https://programmers.co.kr/learn/courses/30/lessons/42576)

```python

from operator import eq

def solution(participant, completion):
    
    answer = []
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    
    flag = True 
    for i in range(len(completion)):
        if not eq(participant[i], completion[i]):
            flag = False
            break
        if flag:
            answer = participant[len(participant)-1]
        
        return answer

# 실패

def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for par, com in zip(participant,completion):
        if par != com:
            return par
    
    return participant[-1]



# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.25ms, 10.8MB)
# 테스트 4 〉	통과 (0.50ms, 11.1MB)
# 테스트 5 〉	통과 (0.49ms, 10.9MB)
# 효율성  테스트
# 테스트 1 〉	통과 (39.72ms, 87.5MB)
# 테스트 2 〉	통과 (63.57ms, 125MB)
# 테스트 3 〉	통과 (82.24ms, 155MB)
# 테스트 4 〉	통과 (90.30ms, 168MB)
# 테스트 5 〉	통과 (85.18ms, 167MB)


```

```python
from operator import eq

a와 b사이에 비교를 수행
eq(a,b) => a == b
ne(a,b) => a != b
lt(a,b) => a < b
le(a,b) => a <= b
gt(a,b) => a > b
ge(a,b) => a >= b

```

# [Programmers - 예산] (https://programmers.co.kr/learn/courses/30/lessons/12982)

```python

def solution(d, budget):
    answer = 0
    leng  = 0
    d.sort()
    for i in range(len(d)):
        leng += d[i]
        if leng <= budget:
            answer += 1
        else:
            break
    return answer

# 테스트 1 〉	통과 (0.07ms, 10.6MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.06ms, 10.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.8MB)
# 테스트 5 〉	통과 (0.04ms, 10.8MB)
# 테스트 6 〉	통과 (0.04ms, 10.8MB)
# 테스트 7 〉	통과 (0.05ms, 10.7MB)
# 테스트 8 〉	통과 (0.07ms, 10.8MB)
# 테스트 9 〉	통과 (0.05ms, 10.6MB)
# 테스트 10 〉	통과 (0.05ms, 10.6MB)
# 테스트 11 〉	통과 (0.05ms, 10.8MB)
# 테스트 12 〉	통과 (0.05ms, 10.7MB)
# 테스트 13 〉	통과 (0.05ms, 10.7MB)
# 테스트 14 〉	통과 (0.05ms, 10.8MB)
# 테스트 15 〉	통과 (0.04ms, 10.8MB)
# 테스트 16 〉	통과 (0.05ms, 10.7MB)
# 테스트 17 〉	통과 (0.05ms, 10.7MB)
# 테스트 18 〉	통과 (0.05ms, 10.7MB)
# 테스트 19 〉	통과 (0.05ms, 10.8MB)
# 테스트 20 〉	통과 (0.04ms, 10.8MB)
# 테스트 21 〉	통과 (0.04ms, 10.8MB)
# 테스트 22 〉	통과 (0.05ms, 10.8MB)
# 테스트 23 〉	통과 (0.04ms, 10.8MB)

```

# [Programmers - [1차]다트 게임](https://programmers.co.kr/learn/courses/30/lessons/17682)

```python

# 문자열처리(String Manipulation)
# 1. 앞에서 한글자 씩 잘라서 처리, 또는 간단한 컴파일러를 만들듯이 토큰화와 의미분석을 통해 계산
# 유의할 점) 점수 중에는 한 자리 뿐만 아니라 두 자리인 10점도 포함되어 있기 때문에 한 글자씩 잘라서 처리할 때 유의 해야함 , 토큰화로 처리 할 때는 정규식을 사용하면 비교적 쉽게 잘라낼 수 있음.
# S,D,T는 원점수, 제곱, 세제곱 처리 스타상은 두 배로 계산, 아차상은 마이너스 점수


```

# [Programmers - 실패율] (https://programmers.co.kr/learn/courses/30/lessons/42889)

```python

# 정렬을 이용한 문제풀이
#   1. 주어진 배열의 길이를 이용해 전체 사용자 수를 구함
#   2. stages를 순회하여 각 스테이지에 몇명의 사용자가 도달했는지 세어줌
#   3. 만들어둔 배열(각 스테이지별 사용자 수가 들어있는)을 순회하면서 stages를 참고해 스테이지별 실패율 계산
#   4. 실패율을 구했다면 , 각 스테이지 번호와 묶어서 실패율을 내림차순으로 정렬
#   5. 실패율이 같을 경우 스테이지 번호가 작은 것을 먼저 오도록 정렬

```

# [해설](https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/)

