# 287. Find the Duplicate Number
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for i in nums:
            if i in check:
                return i
            else:
                check.add(i)


answer = Solution()
print(answer.findDuplicate([1, 3, 4, 2, 2]))

# Runtime: 56 ms, faster than 99.94 % of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.6 MB, less than 7.14 % of Python3 online submissions for Find the Duplicate Number.
# Next challenges:
