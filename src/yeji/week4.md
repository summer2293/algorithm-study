# Leetcode [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

```python
"""
Runtime: 68 ms, faster than 97.63% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 15.1 MB, less than 21.43% of Python3 online submissions for Find the Duplicate Number.
"""
class Solution:
    def findDuplicate(self, nums: List[int]):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
```

# Leetcode [350. Intersection of Two Arrays ](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

```python
"""
Runtime: 48 ms, faster than 96.04% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):
        nums1.sort()
        nums2.sort()
        
        i = j = 0
        r = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]: i += 1
            elif nums1[i] > nums2[j]: j += 1
            else: 
                r.append(nums1[i])
                j += 1
                i += 1
        
        return r
```

# Leetcode [921. Minimum Add to Make Parenteses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

```python
"""
Runtime: 24 ms, faster than 99.50% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l = []
        for i in S:
            if l and l[-1] == '(' and i == ')':
                l.pop()
            else:
                l.append(i)
        return len(l)
                
```

# Leetcode [861. Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/)

```python

# 오늘안에 못풀듯...

```