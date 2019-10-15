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
