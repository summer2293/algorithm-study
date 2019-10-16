[**프로그래머스 Queue 프린터**](https://programmers.co.kr/learn/courses/30/lessons/42587)


```python
	# priorities를 input list로 받아 중요도 순서(숫자가 큰 순서)대로 프린트한다. 
	# location에 위치한 원소의 프린트 순서를 return한다.

	def solution(priorities, location):
	    answer = 1
	    templist = []
	    for i in range(len(priorities)):
	        tupl = (priorities[i], i)
	        templist.append(tupl)
	    
	    while len(priorities):
	        candidate = templist[0]
	        del priorities[0]
	        del templist[0]
	        if not priorities:
	            return answer
	        if candidate[0] < max(priorities):
	            templist.append(candidate)
	            priorities.append(candidate[0])
	        else:
	            if candidate[1] == location:
	                return answer
	            answer += 1
```


**[leetcode Queue 933.Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)**

```python
	ping(t): 주어진 list안에서 t-3000보다 크고 t보다 작은 원소의 개수를 return한다.

	class RecentCounter:
	    def __init__(self):
	        self.counter = []

	    def ping(self, t: int) -> int:
	        self.counter.append(t)
	        while t-3000 > self.counter[0]:
	            del self.counter[0]
	        return len(self.counter)
```

**[leetcode Stack 155. Min Stack](https://leetcode.com/problems/min-stack/)**

```python
	# 기본적인 stack을 설계한다.
	
	class MinStack:
	    def __init__(self):
	        """
	        initialize your data structure here.
	        """
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

**[leetcode Stack 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)**

```
	# 주어진 string s에서 괄호가 대칭이면 True, 아니면 False를 return한다.
	
	class Solution:
	    def isValid(self, s: str) -> bool:
	        stack = []
	        for symbol in s:
	            if symbol == '(' or symbol == '{' or symbol == '[':
	                stack.append(symbol)
	            elif len(stack) == 0:
	                return False
	            elif symbol == ')' and stack[-1] == '(':
	                stack.pop()
	            elif symbol == '}' and stack[-1] == '{':
	                stack.pop()
	            elif symbol == ']' and stack[-1] == '[':
	                stack.pop()
	            else:
	                return False
	        if stack:
	            return False
	        return True
```

**[leetcode Dynamic Programming 70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)**

```python
	# n개의 계단을 1칸 혹은 2칸씩만 오를 수 있을 때, 도달 가능한 경로의 수를 구한다.
	
	class Solution:
	    def climbStairs(self, n: int) -> int:
	        path_per_n = [0, 1, 2]
	        for i in range(3, n+1):
	            ith_path = path_per_n[i-2] + path_per_n[i-1]
	            path_per_n.append(ith_path)
	        return path_per_n[n]
```

**[leetcode Dynamic Programming 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)**

```python	
	# 주어진 배열 nums에 대해, 1개 이상의 원소를 포함한 연속된 subarray의 원소들의 합 중 가장 큰 값을 return한다.
	
	class Solution:
	    def maxSubArray(self, nums: List[int]) -> int:
	        subarray = [nums[0]]
	        for i in range(1, len(nums)):
	            temp_max = max(nums[i], nums[i]+subarray[i-1])
	            subarray.append(temp_max)
	        return max(subarray)
```