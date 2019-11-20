# 5week
## 완전탐색

### 모의고사
```python
def solution(answers):
    answer = []
    students = {
        '1': [1, 2, 3, 4, 5],
        '2': [2, 1, 2, 3, 2, 4, 2, 5],
        '3': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    for i in students:
        l = len(answers)
        q, r = (divmod(l, len(students[i])))
        students[i] = students[i] * q + students[i][:r]
        answer.append(len([i for i, j in zip(answers, students[i]) if i == j]))

    return [i + 1 for i, v in enumerate(answer) if max(answer) == v]
```


### 소수찾기
```python
from itertools import chain, combinations, permutations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num // 2):
        if (num % i) == 0:
            return False
    return True


def get_all_order_set(subset):
    result = []
    for i in subset:
        if i:
            per_s = list(permutations(i))
            result += [int(''.join(j)) for j in per_s]
    return set(result)


def solution(numbers):
    ans = 0
    l = list(powerset(numbers))
    all_set = get_all_order_set(l)

    for i in all_set:
        if is_prime(i):
            ans += 1

    return an
```

- 채점하니 두번 툴렸는데 틀린 이유를 모르겠다… pass

## 그래프
```python
class Solution:
    def findJudge(self, N, trust) -> int:
        if N ==1 and trust == []:
            return 1
        not_judge = list(set([i[0] for i in trust]))
        be_trusted = list(set([i[1] for i in trust if i[1] not in not_judge]))
        for p in be_trusted:
            trust_people = list(set([i[0] for i in trust if i[1] == p]))
            if p not in trust_people:
                trust_people.append(p)
                if len(trust_people) == N:
                    return p
        return -1
```
- 다시 풀어야하는데….
```
Runtime:## 1216 ms
, faster than## 5.01%
ofPython3online submissions forFind the Town Judge.
Memory Usage:## 17.3 MB
, less than## 10.00%
ofPython3online submissions forFind the Town Judge.
```
