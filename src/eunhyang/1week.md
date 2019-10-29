# 알고리즘 스터디 1주차 
#study/algorithm

### 20.Valid Parentheses
```python
class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if '()' in s or '[]' in s or '{}' in s:
                s = s.replace('()', '')
                s = s.replace('{}', '')
                s = s.replace('[]', '')
            else:
                break

        ans = True if s == '' else False
        return ans
```

### 155-min stack
```python
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
```


### 933- Number of Recent calls
```python
class RecentCounter:
    queue = []
    def ping(self, t: int) -> int:
        queue.append(t)
        return len([i for i in queue if i >= t - 3000])
```
- 시간초과뜸 -> 수정
```python
class RecentCounter:
    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        while self.pings:
            a = self.pings[0]
            if a < t - 3000:
                self.pings.pop(0)
            else:
                break

        self.pings.append(t)
        return len(self.pings)
```

### 프린트
```python
def solution(priorities, location):
    b = 1
    while priorities:
        a = priorities.pop(0)
        if priorities and a < max(priorities):
            priorities.append(a)
            if location == 0:
                location += len(priorities)
        else:
            if location == 0:
                return b
            b += 1
        location -= 1
```

### 53.Maximum Subarray
[Maximum Subarray - LeetCode](https://leetcode.com/problems/maximum-subarray/)
```python
class Solution:
    def maxSubArray(self, nums) -> int:
        sub_sums = []
        for i in range(len(nums) + 1):
            for j in range(i+1, len(nums) + 1):
                sub_sums.append(sum(nums[i:j]))
        return max(sub_sums)

```
시간초과.. 


### 70.Climbing Stairs

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        a = n // 2
        for two_num in range(a + 1):
            one_num = n - (2 * two_num)
            den = self.fact(one_num + two_num)
            mol = self.fact(one_num) * self.fact(two_num)
            ans = ans + (den / mol)
        return int(ans)

    def fact(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact
```
