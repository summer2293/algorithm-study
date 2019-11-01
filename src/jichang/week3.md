# LeetCode [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

```python
"""
Runtime: 556 ms, faster than 92.29% of Python online submissions for K Closest Points to Origin.
Memory Usage: 17.3 MB, less than 92.45% of Python online submissions for K Closest Points to Origin.
"""
import pytest_watch

points = [[3,3],[5,-1],[-2,4]]
K = 2
output = [[3,3],[-2,4]]

def test_simple():
    assert solution(points, K) == output

def solution(points, K):
    """
    O(nlogn)
    """
    return sorted(points, key=lambda x: x[0]**2+x[1]**2)[:K]


if __name__ == "__main__":
    print(solution(points, K))
    
```


# LeetCode [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

```python
"""
Runtime: 32 ms, faster than 91.90% of Python online submissions for Valid Anagram.
Memory Usage: 13 MB, less than 50.00% of Python online submissions for Valid Anagram.
"""

import pytest_watch

s = "anagram"
t = "nagaram"
output = True


def test_simple():
    assert solution(s, t) == output

def solution(s, t):
    answer = dict()
    for i in s:
        try:
            answer[i] += 1
        except:
            answer[i] = 1
    
    for i in t:
        try:
            if answer[i] > 1:
                answer[i] -= 1
            else:
                answer.pop(i)
        except:
            return False
    return not bool(answer)

if __name__ == "__main__":
    print(solution(s, t))

```

# LeetCode [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

```python
"""
Runtime: 12 ms, faster than 96.10% of Python online submissions for Last Stone Weight.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Last Stone Weight.
"""

import pytest_watch

stones = [2,7,4,1,8,1]
output = 1


def test_simple():
    assert solution(stones) == output

def solution(stones):
    while len(stones) > 1:
        stones.sort()
        heaviest = stones.pop()
        next_heaviest = stones.pop()

        if heaviest == next_heaviest:
            pass
        else:
            stones.append(heaviest-next_heaviest)
    if stones:
        return stones[0]
    return 0

```

# LeetCode [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

```python
"""
Runtime: 84 ms, faster than 93.45% of Python online submissions for Top K Frequent Elements.
Memory Usage: 15.4 MB, less than 36.59% of Python online submissions for Top K Frequent Elements.
"""

import pytest_watch
import operator

nums = [4,1,-1,2,-1,2,3]
k = 2
output = [-1, 2]

def test_simple():
    assert solution(nums, k) == output

def solution(nums, k):
    answer = dict()

    for i in nums:
        try:
            answer[i] += 1
        except:
            answer[i] = 1
    
    sorted_answer = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)

    answer = list()
    for i in sorted_answer:
        answer.append(i[0])
        if len(answer) >= k:
            return answer

```