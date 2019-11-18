완전탐색 - 프로그래머스 - 모의고사

```python
# answers = [1, 2, 3, 4, 5]
# answers = [1, 3, 2, 4, 2]
# result = [1]
# result = [1, 2, 3]

def solution(answers):
    abandoner_a = [1, 2, 3, 4, 5]
    abandoner_b = [2, 1, 2, 3, 2, 4, 2, 5]
    abandoner_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    new_a = list()
    new_b = list()
    new_c = list()

    a = 0
    b = 0
    c = 0

    for i in range(len(answers)):
        new_a.append(abandoner_a[i%5])
        new_b.append(abandoner_b[i%8])
        new_c.append(abandoner_c[i%10])
    
    for i in range(len(answers)):
        if new_a[i] == answers[i]:
            a += 1
        if new_b[i] == answers[i]:
            b += 1
        if new_c[i] == answers[i]:
            c += 1
    
    answer = list()
    max_person = max(a, b, c)

    if max_person == a:
        answer.append(1)
    if max_person == b:
        answer.append(2)
    if max_person == c:
        answer.append(3)
        
    return answer
```

완전탐색 - 프로그래머스 - 소수찾기

```python
import itertools
import math

def solution(numbers):
    answer = set()
    number = [i for i in numbers]
    for i in range(1, len(number)+1):
        a = list(itertools.permutations(number, i))
        for j in a:
            aa = ""
            for k in j:
                aa += k
            if is_prime(int(aa)):
                answer.add(int(aa))
    return len(answer)



def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
```
