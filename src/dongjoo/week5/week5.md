## 완전탐색

##### 수포자

```python
def solution(answers):
    num_correct = [0, 0, 0]
    pattern_one = [1,2,3,4,5]
    pattern_three = [3,3,1,1,2,2,4,4,5,5]
    pattern_two = [2,1,2,3,2,4,2,5]
    q_idx = 0
    for question in answers:
        if question == pattern_one[q_idx % len(pattern_one)]:
            num_correct[0] += 1
        if question == pattern_two[q_idx % len(pattern_two)]:
            num_correct[1] += 1
        if question == pattern_three[q_idx % len(pattern_three)]:
            num_correct[2] += 1
        q_idx += 1
    maximum = max(num_correct)
    answer = [i for i in range(1,4) if num_correct[i-1] == maximum]
    return answer
```

##### 소수 찾기

```python

from collections import Counter


def solution(numbers):
    answer = 0
    return answer


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, round(number ** 0.5)+1):
        if number % i == 0:
            # print("factor is ", i)
            return False
    return True


# probably has horrible performance
def combi_dfs(counts, curr_selected, total_selected, total):
    # counts is counter, curr_selected is Counter of selected stuff
    # total_selected is list of selected sets, total is num of selections
    if sum(counts.values()) == 0:
        # print("empty potentials!!!")
        return
    if sum(curr_selected.values()) == total:
        if curr_selected not in total_selected:
            # print(total_selected)
            total_selected.append(curr_selected)
            curr_selected = Counter()
        return
    for key in counts:
        # add elements to curr_selected
        if counts[key] > 0:
            curr_selected[key] += 1
            # after adding, decrement counts
            counts[key] -= 1
            combi_dfs(counts.copy(), curr_selected, total_selected, total)
            curr_selected = Counter() # reset curr_selected

# 푸는 중
```
##### 숫자 야구

```python
def solution(baseball):
    answer = 0
    return answer
```

## graph

##### find town judge

```python

from typing import List
# first implementation without using graph


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted_by = dict()
        # for loop to make potential judge sets
        for pair in trust:
            if pair[1] in trusted_by:
                trusted_by[pair[1]].add(pair[0])
            else:
                trusted_by[pair[1]] = set([pair[0]])

        # print(trusted_by, "trusted by")

        maximum = None
        max_len = 0
        # find the potential judge by running max for number of elements in set
        for person in trusted_by:
            if len(trusted_by[person]) > max_len:
                maximum = person
                max_len = len(trusted_by[person])

        # print(maximum, "max")
        # edge case for only one potential judge
        if len(trusted_by) == 1:
            return list(trusted_by.keys())[0]

        for person in trusted_by:
            # check if set contains something else not in "judge set"
            if len(trusted_by[person] - trusted_by[maximum]): 
                return -1
            if trusted_by[person] == trusted_by[maximum] and person != maximum:
                return -1
        if maximum == None:
            return N
        return maximum

answer = Solution()
print(answer.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))

# Runtime: 772 ms, faster than 99.00 % of Python3 online submissions for Find the Town Judge.
# Memory Usage: 17.2 MB, less than 10.00 % of Python3 online submissions for Find the Town Judge.
```

##### regions cut by slashes

```python
# ?
````



