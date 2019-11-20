class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for elem in nums:
            answer = answer ^ elem
        return answer


# result: 
# first try
# Runtime: 100 ms, faster than 71.96 % of Python3 online submissions for Single Number.
# Memory Usage: 16.3 MB, less than 6.56 % of Python3 online submissions for Single Number.
