from typing import List
# 350. Intersection of Two Arrays II
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_one = Counter(nums1)
        nums_two = Counter(nums2)
        return [elem for elem in (nums_one & nums_two).elements()]


answer = Solution()
print(answer.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

# Runtime: 40 ms, faster than 99.86 % of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 12.8 MB, less than 100.00 % of Python3 online submissions for Intersection of Two Arrays II.
# Next challenges:
