# 350.Intersection of Two Arrays II.py
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# first code
import collections
import bisect
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        list = []
        nums1.sort()
        nums2.sort()
        # len 비교
        if len(nums1) > len(nums2):
            s,b = nums2, nums1
        else:
            b,s = nums1, nums2
        
        for i in s:
            if i in b:
                list.append(i)
                b.remove(i)
        
        return list
     
            