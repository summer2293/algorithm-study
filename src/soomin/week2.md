# single number

>  풀었던 코드들이 다 시간초과 ㅠ__ㅠ 솔루션 봤더니 try, exception 을 써서 그렇게 바꾸니 성공했당

```python
class Solution(object):
    def singleNumber(self, nums):
        tmp = {}
        for i in nums:
            try: 
                del tmp[i]
            except:
                tmp[i] = 0
                
        for i in tmp:
            return i
        
# first - 시간 초과 
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         tmp = {}
#         for i in nums:
#             if i not in tmp.keys():
#                 tmp[i] = 0
#             else:
#                 del tmp[i]        
#         for i in tmp:
#             return i
                
```



# Two sum

```python
class Solution(object):
    def twoSum(self, nums, target):
        data = {}
        for i,v in enumerate(nums):
            print(i,v)
            n = target - v
            
            if n in data:
                return[data[n], i]
            else:
                data[v] = i
```



# Maximum Depth of Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print(root)
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
  
     
```



# merge-two-binary-trees

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        result = TreeNode(t1.val + t2.val)
        result.left = self.mergeTrees(t1.left, t2.left)
        result.right = self.mergeTrees(t1.right, t2.right)
        
        return result
```

