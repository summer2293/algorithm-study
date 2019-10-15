# maximum-subarray
​
```python
import pytest_watch
​
input = [-2, 1, -3, 4, -1, 2, 1, -5, 4, -1, -1]
output = 6
​
"""
구글링함
i번째 원소에 대해
i번 이전의 연속합 + i번째 원소 vs i번째 원소 큰 값 가져옴
​
dp [-2, 1, -2, 4, 3, 5, 6, 1, 5, 4, 3]
​
"""
​
def test_simple():
    assert solution(input) == output
​
​
def solution(nums):
    output = nums[0]
    max = nums[0]
    dp = nums[:1]
    for idx, value in enumerate(nums[1:]):
        if value > dp[idx] + value:
            dp.append(value)
            output = value
            if output > max:
                max = output
        else:
            dp.append(dp[idx]+value)
            output = dp[idx]+value
            if output > max:
                max = output
    return max
        
​
if __name__ == "__main__":
    solution(input)
```
​
# climbing-stairs
​
```python
import pytest_watch
​
input = 3
output = 3
​
"""
4
1+1+2
2+2
​
1+1+1+1
1+2+1
2+1+1
"""
def test_simple():
    assert solution(input) == output
​
​
def solution(input):
    dp = [0, 1, 2]
    for i in range(3, input+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[input]
​
```
​
# valid-parentheses
​
```python
import pytest_watch
​
s = "()[]{}"
output = True
​
​
def test_simple():
    assert solution(s) == output
​
def solution(s):
    stack = list()
    for i in s:
        if i == ')':
            if not len(stack) or stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif i == '}':
            if not len(stack) or stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif i == ']':
            if not len(stack) or stack[-1] != '[':
                return False
            else:
                stack.pop()
        else:
            stack.append(i)
    if len(stack):
        return False
    return True
​
```
​
# min-stack
​
```python
"""
getmin 메소드의 수행 시간을 o(1)로 줄였습니다.
"""
class MinStack:
    def __init__(self):
        self.minstack = list()
        self.min = list()
    
    def push(self, x:int) -> None:
        self.minstack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            if self.min[-1] >= x:
                self.min.append(x)
    
    def pop(self) -> None:
        pop_ele = self.minstack.pop()
        if pop_ele == self.min[-1]:
            self.min.pop()
        
    
    def top(self) -> int:
        return self.minstack[-1]
​
    def getMin(self) -> int:
        return self.min[-1]
​
​
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()   # --> Returns -3.
    minStack.pop()
    minStack.top()      # --> Returns 0.
    minStack.getMin()   # --> Returns -2.
​
```
​
# number-of-recent-calls
​
```python
"""
단순히 list를 deque로 바꾸기만해도 속도가 향상된다!
"""
​
​
from collections import deque
​
​
class RecentCounter:
    def __init__(self):
        self.obj = deque()
        
​
    def ping(self, t: int) -> int:
        if t:
            self.obj.append(t)
            while True:
                if self.obj[0] < t-3000:
                    self.obj.popleft()
                else:
                    return len(self.obj)
        else:
            return 'null'
​
​
if __name__ == "__main__":
​
    obj = RecentCounter()
    print(obj.ping(1))
    print(obj.ping(100))
    print(obj.ping(3001))
    print(obj.ping(3002))
```
​
# 프린터
​
```python
import pytest_watch
​
priorities = [1, 1, 9, 1, 1, 1]	
location = 0
output = 5
​
​
def test_simple():
    assert solution(priorities, location) == output
​
"""
[[2, 1, 3, 2],
[0, 1, 2, 3]]
​
[[1, 3, 2, 2],
[1, 2, 3, 0]]
​
[[3, 2, 2, 1],
[2, 3, 0, 1]]
​
전체 len - 현재 len + 1
​
[[1, 1, 9, 1, 1, 1],
[0, 1, 2, 3, 4, 5]]
​
[[1, 9, 1, 1, 1, 1],
[1, 2, 3, 4, 5, 0]]
​
[[9, 1, 1, 1, 1, 1],
[2, 3, 4, 5, 0, 1]]
​
[[1, 1, 1, 1, 1],
[3, 4, 5, 0, 1]]
​
[[1, 1, 1, 1],
[4, 5, 0, 1]]
​
[[1, 1, 1],
[5, 0, 1]]
​
[[1, 1],
[0, 1]]
​
전체 len - 현재 len + 1
6 - 2 + 1 = 5
​
"""
​
"""
123
​
231
​
a[:-1]
"""
​
def sol(priority_2d, location):
    if priority_2d[0][0] == max(priority_2d[0]) and priority_2d[1][0] == location:
        return len(priorities) - len(priority_2d[0]) + 1
    if priority_2d[0][0] == max(priority_2d[0]):
        priority_2d[0].pop(0)
        priority_2d[1].pop(0)
        return sol(priority_2d, location)
    priority_2d[0] = priority_2d[0][1:] + priority_2d[0][:1]
    priority_2d[1] = priority_2d[1][1:] + priority_2d[1][:1]
    return sol(priority_2d, location)
​
​
def solution(priorities, location):
    priority_2d = [priorities, [i for i in range(len(priorities))]]
    return sol(priority_2d, location)
​
​
if __name__ == "__main__":
    solution(priorities, location)
​
```
