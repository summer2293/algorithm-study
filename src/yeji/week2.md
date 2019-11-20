# 1. Two Sum

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) :
        i = 0
        j = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[i] == nums[j] and i != j:
                    return [i,j]
            
```

# 136. Single Number  

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]
        return nums[-1]
```

# 617. Merge Two Binary Trees

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None :
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val;
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
       
``` 

# 104. Maximum Depth of Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0
        if self.maxDepth(root.left) is None and self.maxDepth(root.right) is None :
            return 1
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
```





