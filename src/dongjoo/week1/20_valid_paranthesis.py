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
