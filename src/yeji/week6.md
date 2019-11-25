# [leetcode-Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode):
        return self.isMirror(root,root)
    
    def isMirror(self,t1,t2):
        if not t1 and not t2 : return True
        if not t1 or not t2: return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

# Runtime: 36 ms, faster than 84.29% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.   
```

# [leetcode-Course Schedule](https://leetcode.com/problems/course-schedule/)

```python

```

# [leetcode-Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node'):
        if not root:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            new_queue = []
            for q in queue:
                if not q.children:
                    continue
                new_queue.extend(q.children)
            queue = new_queue
        return depth

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node'):
        if not root : return 0
        if not root.children : return 1
        height = 0
        for node in root.children:
            height = max(self.maxDepth(node), height)
            print(height)
        return height + 1

# Runtime: 60 ms, faster than 95.60% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Maximum Depth of N-ary Tree.
```