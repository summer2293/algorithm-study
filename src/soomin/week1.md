## stack

##### valid-parentheses

```python
class Solution:
    def isValid(self, s: str) -> bool:
        left = list()
        valid = ""
        for i in s:
            if left: 
                valid = left[-1] + i
            if (i in "([{"): 
                left.append(i)
            elif (valid =="()" or valid == "{}" or valid == "[]"):
                left.pop()
                valid = ""
            else:
                return False
        if (left):
            return False
        else:
            return True
```

##### min-stack

```python
class MinStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> None:
        return self.q.pop()

    def top(self) -> int:
        return self.q[len(self.q)-1]
    
    def getMin(self) -> int:
        return min(self.q)
```



## queue

##### printer

```python
def solution(priorities, location):
    answer = 0
    m = max(priorities)
    while True:
        value = priorities.pop(0)
        if m == value:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(value)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer
```

##### Number of Recent Calls

```python
# 문제 이해를 잘 못했나봄 ㅠㅠ 솔루션 코드로 이해 
class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)

        while self.q[0] < t-3000:
            self.q.popleft()
            print(self.q)
        return len(self.q)
  # 망한코드 
  #class RecentCounter:

  #   def __init__(self):
  #      self.q = []

  #  def ping(self, t: int) -> int:
  #      self.q.append(t)
  #      print(self.q)
  #      count = 0 
  #      for i in self.q:
  #          if i < t - 3000:
  #              self.q.remove(i)
  #
  #    return len(self.q)

```



## dp

##### climbing-stairs

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1
        first = 1
        second = 2
        
        # python 은 n까지 > n+1 
        for i in range(3,n+1):
            third = first + second
            first, second = second, third 
        
        return second
```

##### number-of-recent-calls

```python
# 내가한거 time exceed ㅠ____ㅠ
# 찾아보고 이해한 코드! 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # default  
        max_num = nums[0]
        point = 0
        
        for num in nums:
            # num 더하기 
            point += num
            if point > max_num:
                max_num = point
            # 음수값일경우 누적 >  작아지므로 0 으로 변경 
            if point < 0:
                point = 0
 
        return max_num
```

