# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         lst_a = list(s)
#         lst_b = list(t)
#         if sorted(lst_a) == sorted(lst_b):
#             return True
#         return False

# 1st attempt:
# Runtime: 68 ms, faster than 38.90 % of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.5 MB, less than 6.25 % of Python3 online submissions for Valid Anagram.
# comments: tried to use set for O(n) time, didn't work used sorting instead
# can probably use counting sort to drop the time down to O(n)?


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         a = dict()
#         b = dict()
#         for c in s:
#             if c in a:
#                 a[c] += 1
#             else:
#                 a[c] = 1
#         for c in t:
#             if c in b:
#                 b[c] += 1
#             else:
#                 b[c] = 1
#         return a == b

# 2nd attempt:
# Runtime: 52 ms
# Memory Usage: 14.1 MB
# 78.19%
# comments for 3rd attempt, could probably lower space complexity by only using one dict


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         a = dict()
#         for c in s:
#             if c in a:
#                 a[c] += 1
#             else:
#                 a[c] = 1
#         for elem in t:
#             if elem in a:
#                 a[elem] -= 1
#                 if a[elem] < 0:
#                     return False
#             else:
#                 return False
#         for value in a.values():
#             if value > 0:
#                 return False
#         return True


# Runtime: 52 ms, faster than 78.19 % of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.1 MB, less than 9.38 % of Python3 online submissions for Valid Anagram.
# hmm.. absolutely no difference in memory

#idea for improvement: use collections counter?


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

# Runtime: 48 ms, faster than 85.87 % of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.2 MB, less than 6.25 % of Python3 online submissions for Valid Anagram.
# Next challenges:
