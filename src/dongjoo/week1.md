# recent-counter
```python
# ----Question 1
# 1st attempt
from collections import deque

class RecentCounter:

    def __init__(self):
        self.que = deque()
        

    def ping(self, t: int) -> int:
        self.que.append(t)
        while (self.que)[0] < t - 3000:
            # print(self.que, "que", t-3000)
            self.que.popleft()
        return len(self.que)

# commands = ["ping","ping","ping","ping"]
# inputs = [[1],[100],[3001],[3002]]
# answer = RecentCounter()

# for i in range(len(commands)):
#     operation = "answer." + str(commands[i]) + "(" + str(inputs[i][0]) + ")"
#     # print(operation)
#     print(eval(operation))

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Result:
# Runtime: 324 ms, faster than 98.24 % of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 18.5 MB, less than 20.00 % of Python3 online submissions for Number of Recent Calls.
```
# printer
``` python
from collections import deque
def solution(priorities, location):
    answer = 0
    # index variable to keep track of "location"
    idx = location
    queue = deque(priorities)
    stack = sorted(priorities)
    while queue:
        print("stack", stack)
        print("q", queue)
        print(answer, idx, "answer, idx")
        elem = queue.popleft()
        if elem != stack[-1]:
            queue.append(elem)
            # decrease index of important file
            idx -= 1
            if idx < 0:
                idx = len(queue) - 1
        else:
            stack.pop()
            idx -= 1
            answer += 1
            if idx < 0:
                return answer
    return answer


answer = solution([1, 1, 9, 1, 1, 1],0)
# answer = solution([2, 1, 3, 2],2)

print(answer)


# ----Question 2
# kinda difficult because have to keep count of what the 
# "maximum" priority is to decide whether to send to back or not
# can be done in a lot of ways but did it with a stack that's 
# basically a sorted priorities, popping the "max" if the element
# at the "head" of queue has "max priority"
# space complexity o(n) for stack
# Time complexity o(nlogn) for sort

# maybe explain that deque can't be mutated during iteration
# to fellow study members

```
# minstack
```python
# ----Question 1
# 1st attempt
# couldn't think of way to get min in constant time
# but utilized a minimum variable and the index that points to that
# in order to keep track of when the min gets popped and recalculate
# minimum if minimum gets popped
# this will yield n squared time when the input is given in 
# decreasing order and pop and getMin are alternately called

class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = None
        self.minindex = None
    def push(self, x: int) -> None:
        # print("push, stack", self.stack)
        self.stack.append(x)
        if len(self.stack) == 1:
            self.minindex = 0
            self.minimum = x
        else:
            if x < self.minimum:
                self.minimum = x
                self.index = len(self.stack)-1
    def pop(self) -> None:
        # print("pop, stack", self.stack)
        self.stack.pop()
        # recalculate min when minimum gets popped and stack isn't empty
        if len(self.stack) >= self.minindex and self.stack:
            # start again from 0 to find min
            self.minimum = self.stack[0]
            self.minindex = 0
            for idx in range(len(self.stack)):
                if self.stack[idx] < self.minimum:
                    self.minimum = self.stack[idx]
                    self.minindex = idx
        elif not self.stack:
            self.minimum = None
            self.minindex = None
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minimum

        
answer = MinStack()
answer.push(-2)
answer.push(0)
answer.push(-3)
print(answer.getMin())
answer.pop()
print(answer.top())
print(answer.getMin())

["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[[], [-2], [0], [-3], [], [], [], []]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# some other guy's answer, really smart
# class MinStack:

# def __init__(self):
#     self.q = []

# # @param x, an integer
# # @return an integer


# def push(self, x):
#     curMin = self.getMin()
#     if curMin == None or x < curMin:
#         curMin = x
#     self.q.append((x, curMin))

# # @return nothing


# def pop(self):
#     self.q.pop()


# # @return an integer
# def top(self):
#     if len(self.q) == 0:
#         return None
#     else:
#         return self.q[len(self.q) - 1][0]


# # @return an integer
# def getMin(self):
#     if len(self.q) == 0:
#         return None
#     else:
#         return self.q[len(self.q) - 1][1]


```

# valid-parentheis
```python
# 1. attempt
# class Solution:
#     def isValid(self, s: str) -> bool:
#         left = ["(", "{", "["]
#         right = [")", "}", "]"]
#         stack = []
#         for elem in s:
#             if elem in left:
#                 stack.append(elem)
#                 # print(stack, "stack")
#             elif elem in right:
#                 if not stack:
#                     return False
#                 check = stack.pop()
#                 # print('elif', elem, left.index)
#                 if left.index(check) != right.index(elem):
#                     return False
#         if stack:
#             return False
#         return True
# Runtime: 40 ms, faster than 47.51 % of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 5.22 % of Python3 online submissions for Valid Parentheses.

# maybe use a dictionary for constant lookup for matching paranthesis?
# if the index operation that is at worst o(3) that important?


# 2nd attempt
# class Solution:
#     def isValid(self, s: str) -> bool:
#         matches = {")":"(", "}":"{", "]":"["}
#         stack = []
#         for elem in s:
#             if elem not in matches:
#                 stack.append(elem)
#             else:
#                 if not stack:
#                     return False
#                 if stack[-1] != matches[elem]:
#                     return False
#                 stack.pop()
#         if stack:
#             return False
#         return True

# Runtime: 40 ms, faster than 47.51 % of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 5.22 % of Python3 online submissions for Valid Parentheses.

# improvement: maybe use ascii code?
# maybe use array instead of list? 

# "(": 40, ")": 41, "{": 123 "}":125 "[": 91 "]":93
# 3rd attempt
from timeit import timeit

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for elem in s:
            if ord(elem) == 40 or ord(elem) == 123 or ord(elem) == 91:
                stack.append(elem)
            else:
                if not stack:
                    print("not stack")
                    return False
                if ord(elem) != ord(stack[-1])+1 and ord(elem) != ord(stack[-1])+2:
                    return False
                stack.pop()
        if stack:
            return False
        return True

sol = Solution()
answer = sol.isValid("()")
print(answer)

# Runtime: 36 ms, faster than 78.26 % of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 5.22 % of Python3 online submissions for Valid Parentheses.

# some other guy's answer, 20 ms, using sets
# class Solution(object):
#     def isValid(self, s):

#         if len(s) % 2 != 0:
#             return False
#         opening = set('([{')
#         matches = set([('(', ')'), ('[', ']'), ('{', '}')])
#         stack = []

#         for paren in s:
#             if paren in opening:
#                 stack.append(paren)
#             else:
#                 if len(stack) == 0:
#                     return False
#                 last_open = stack.pop()
#                 if (last_open, paren) not in matches:
#                     return False
#         return len(stack) == 0




```
# max-subarray
```python

# ----Question 1

# 1st attempt


# class Solution:
#     def maxSubArray(self, nums):
#         # use input to save space, for memoization
#         for i in range(1, len(nums)):
#             nums[i] = max(nums[i], nums[i] + nums[i-1])
#         return max(nums)



# result:
# Runtime: 76 ms, faster than 78.17 % of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.8 MB, less than 5.69 % of Python3 online submissions for Maximum Subarray.
# time is fast, but how should i decrease memory?
# improvement: can i increase time by keeping a max pointer?

# 2nd attempt, with max pointer
class Solution:
    def maxSubArray(self, nums):
        # use input to save space, for memoization
        maximum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            maximum = max(nums[i], maximum)
        return maximum

# result: not faster at all....
# Runtime: 76 ms, faster than 78.17 % of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.8 MB, less than 5.69 % of Python3 online submissions for Maximum Subarray.


# afterthought, realized you don't need the whole array,
# maybe decrease memory usage that way?
# but isn't the memory the same? since you can't "delete" the input array?

# below is someone else's answer of my afterthought
# found solution after i had already thought of it, 
# independent thought

# class Solution:
#     # @param A, a list of integers
#     # @return an integer
#     # 6:57
#     def maxSubArray(self, A):
#         if not A:
#             return 0

#         curSum = maxSum = A[0]
#         for num in A[1:]:
#             curSum = max(num, curSum + num)
#             maxSum = max(maxSum, curSum)

#         return maxSum


```
# climbing-stairs
```python

# dp 몰랐을 때, 예전 0th try

# 70. Climbing Stairs
# from math import factorial as fac


# class Solution:
#   def climbStairs(self, n):
#     if n == 1:
#       return 1
#     if n == 2:
#       return 2
#     max_two = n//2
#     max_one = n
#     ways = 0
#     for i in range(0, max_two+1):

#       ways += fac(max_one-i)/(fac(max_one-2*i) * fac(i))

#     return int(ways)



# 1st try after learning about dp
# 70. Climbing Stairs
# class Solution:
#     def __init__(self):
#         self.memo = []
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         self.memo = [0] * (n+1)
#         self.memo[0] = 1
#         self.memo[1] = 1
#         self.memo[2] = 2
#         # print(self.memo)
#         for i in range(2,n+1):
#             self.memo[i] = self.memo[i-1] + self.memo[i-2]
#             # print(self.memo)
#         # print(self.memo)
#         return self.memo[n]


# Result:

# 45 / 45 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.8 MB
# 67.17%

# 2nd solution: try to speed up by not using list read and write, 
# no list initialization, 

class Solution:
    def climbStairs(self, n):
        if n < 3:
            return n
        prev_one = 1
        prev_two = 2
        answer = None
        for _ in range(2,n):
            answer = prev_one + prev_two
            prev_one = prev_two
            prev_two = answer
            print(prev_one, prev_two, answer)
        return prev_two

# Result:
# Runtime: 36 ms, faster than 67.17 % of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 5.97 % of Python3 online submissions for Climbing Stairs.

# some other guy's smart answer
# https://leetcode.com/problems/climbing-stairs/discuss/25436/Using-the-Fibonacci-formular-to-get-the-answer-directly

```