## Graph
**[leetcode Graph 997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)**
```python
# 마을에 있는 한 사람의 judge를 찾아서 반환. 없다면 -1을 반환
# Runtime: 848 ms, faster than 66.14% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 17.2 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        candidates = list(range(1, N+1))
                for i in range(len(trust)):
                    if trust[i][0] in candidates:
                        candidates.remove(trust[i][0])
                if candidates:
                    for candi in candidates:
                        check = 0
                        for i in range(len(trust)):
                            if trust[i][1] == candi:
                                check += 1
                        if check == N-1:
                            return candi
                    return -1
                else:
                    return -1

# Runtime: 784 ms, faster than 97.89% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 17.2 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1:
            return 1
        info = [0]*(N+1)
        for i, j in trust:
            info[i] -= 1
            info[j] += 1
        for candi in info:
            if candi == N-1:
                return info.index(candi)
        return -1
```

**[leetcode Graph 959. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/)**
```python
# grid는 '/', '\', ' '로 구성되어 있는 정사각형이다. 구분선에 의해 잘라지는 영역의 개수를 반환
# 너무 어려워서 내일까지 풀어 보겠습니다 ㅠㅠ
```

## Brute Force
**[프로그래머스 완전탐색 모의고사](https://programmers.co.kr/learn/courses/30/lessons/42587)**
```python
# 답을 찍는 특정 패턴을 가지는 사용자 1, 2, 3 중 정답을 가장 많이 맞힌 사람을 list로 반환

def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_score = 0
    b_score = 0
    c_score = 0
    for i in answers:
        temp_a = a.pop(0)
        temp_b = b.pop(0)
        temp_c = c.pop(0)
        if i == temp_a:
            a_score += 1
        if i == temp_b:
            b_score += 1
        if i == temp_c:
            c_score += 1
        a.append(temp_a)
        b.append(temp_b)
        c.append(temp_c)
    maxi = max(a_score, b_score, c_score)
    if a_score == maxi:
        answer.append(1)
    if b_score == maxi:
        answer.append(2)
    if c_score == maxi:
        answer.append(3)
            
    return answer
```

**[프로그래머스 완전탐색 소수찾기](https://programmers.co.kr/learn/courses/30/lessons/42839)**
```python
# 주어진 string numbers를 한 자리씩 분리해서 숫자를 조합할 수 있다. 만들 수 있는 조합 중 소수의 개수를 반환
from itertools import permutations #가능한 모든 순열을 구하게 해준다

def check_primes(n, t_set, answer): #n은 set중 가장 큰 숫자, t_set은 확인할 set
    sieve = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if sieve[k]:
            sieve[k*2::k] = [False] * ((n - k) // k)
    for x in t_set:
        if sieve[x]:
            answer += 1
    return answer

def solution(numbers):
    a = list(numbers)
    total = []
    for i in range(1, len(a)+1):
        temp = list(permutations(a, i))
        for j in range(len(temp)):
            comb = ''
            for k in range(i):
                comb += temp[j][k]
            total.append(comb)
    
    t_set = set([int(i) for i in total])
    return check_primes(max(t_set), t_set, 0)
```

**[프로그래머스 완전탐색 숫자 야구](https://programmers.co.kr/learn/courses/30/lessons/42841)**
```python
# 숫자야구에 대한 답 후보의 개수를 반환.
from itertools import permutations

def solution(baseball):
    answer = 0
    candidates = list(permutations(['1','2','3','4','5','6','7','8','9'], 3))
    for candi in candidates: # 순열 중 한 개
        check = True

        for curve in baseball: # 뽑힌 숫자열에 대해 검사
            strike = 0
            ball = 0
            nums = list(str(curve[0]))

            for i in range(3):
                for j in range(3):
                    print(candi[i], nums[j])
                    if candi[i] == nums[j] and i == j:
                        strike += 1
                    if candi[i] == nums[j] and i != j:
                        ball += 1
                        
            if curve[1] != strike or curve[2] != ball: 
                check = False #하나라도 다르다면 answer에서 제외

        if check:
            answer += 1
                
    return answer

```

**[프로그래머스 완전탐색 카펫](https://programmers.co.kr/learn/courses/30/lessons/42842)**
```python
# 주어진 list nums는 n+1개의 원소가 존재하고, 각 원소는 1~n사이의 값을 가진다.
def factorization(red):
    aliquot = []
    for i in range(1,int(red**0.5)+1):
        if red % i == 0:
            aliquot.append(i)
            aliquot.append(red//i)
    return aliquot
            
def solution(brown, red):
    width = sorted(factorization(red))
    size = len(width)
    for i in range(size):
        if width[-(i+1)]*2 + width[i]*2 + 4 == brown:
            return [width[-(i+1)]+2, width[i]+2]
```


