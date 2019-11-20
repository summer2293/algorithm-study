## 완전탐색 - 프로그래머스 - 모의고사

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

## 완전탐색 - 프로그래머스 - 소수찾기

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

## 완전탐색 - 프로그래머스 - 숫자야구

```python
import pytest_watch

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
output = 2


def test_simple():
    assert solution(input) == output


def make_valid_number_list(numbers):
    results = list()
    for i in numbers:
        if ('0' not in i) and i[0] != i[1] and i[0] != i[2] and i[1] != i[2]:
            results.append(i)
    return results


def solution(baseball):
    candidates = [str(i) for i in range(111, 1000)]
    candidates = make_valid_number_list(candidates)
    answer = set(candidates)

    for game in baseball:
        temp_answer = set()
        for candidate in candidates:
            game_number = str(game[0])
            strike = 0
            ball = 0
            for idx, value in enumerate(game_number):
                if value in candidate:
                    if value == candidate[idx]:
                        strike += 1
                    else:
                        ball += 1
            if game[1] == strike and game[2] == ball:
                temp_answer.add(candidate)
        answer = answer & temp_answer
    return len(answer)


if __name__ == "__main__":
    solution(baseball)
```


## 그래프 - 리트코드 - find-the-town-judge

```python
import pytest_watch

N, trust = 11, [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]
output = -1


def test_simple():
    assert solution(N, trust) == output

def solution(N, trust):
    if N == 1:
        return 1
    answer = -1
    graph = [[] for _ in range(N+1)]
    for pair in trust:
        graph[pair[0]].append(pair[1])
    for idx, value in enumerate(graph):
        if idx != 0 and len(value) == 0:
            for jdx, jvalue in enumerate(graph[1:]):
                if idx != jdx+1:
                    if idx not in jvalue:
                        answer = -1
                        break
                    else:
                        answer = idx
            if answer != -1:
                return answer
    return answer


if __name__ == "__main__":
    solution(N, trust)

```


## 완전탐색 - 프로그래머스 - 카펫

```python
import pytest_watch

brown, red = 18, 12
output = [6, 5]


def test_simple():
    assert solution(brown, red) == output


def solution(brown, red):
    total_carpet = brown+red
    for i in range(3, int(total_carpet ** 0.5)+1):
        if total_carpet % i == 0:
            height = i
            width = total_carpet // i
            for j in range(2, min(height, width), 2):
                if height-j < 1 or width-j < 1:
                    break
                if (height-j) * (width-j) == red:
                    return [max(height, width), min(height, width)]
    return -1

if __name__ == "__main__":
    solution(brown, red)

```