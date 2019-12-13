## DFS

##### symmetric tree

```python
from collections import deque
class Solution:
    def __init__(self):
        self.q = deque()

    def lstSymmetric(self, lst):
        length = len(lst)//2
        for idx in range(length):
            if lst[idx] == None and lst[-(idx+1)]== None:
                continue
            if lst[idx] != None and lst[-(idx+1)] != None:
                if lst[idx].val != lst[-(idx+1)].val:
                    return False
            else:
                return False
        return True

    def levelTraversal(self):
        if not self.q:
            return True
        level_q = []
        while self.q:
            temp = self.q.popleft()
            if temp == None:
                continue
            level_q.append(temp.left)
            level_q.append(temp.right)
        # print('level q', level_q)
        if self.lstSymmetric(level_q):
            self.q = deque(level_q)
            return self.levelTraversal()
        else:
            # print('else level 1', level_q)
            # print("else false")
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        self.q.append(root)
        return self.levelTraversal()


answer = Solution()
print(answer.isSymmetric(root), "is the answer")

# Runtime: 40 ms, faster than 65.22 % of Python3 online submissions for Symmetric Tree.
# Memory Usage: 12.7 MB, less than 100.00 % of Python3 online submissions for Symmetric Tree.
```

##### courses

```python


```


## BFS

##### binary-tree-level-order-traversal

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import deque
class Solution:
    def __init__(self):
        self.q = deque()
        self.level_order = []
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.q.append(root)
        self.level_order.append([root.val])
        self.levelTraversal()
        return self.level_order
    def levelTraversal(self):
        if len(self.q) == 0:
            return
        level = []
        children_queue = deque()
        while self.q:
            temp = self.q.popleft()
            if temp.left:
                level.append(temp.left.val)
                children_queue.append(temp.left)
            if temp.right:
                level.append(temp.right.val)
                children_queue.append(temp.right)
        self.q = children_queue
        if level:
            self.level_order.append(level)
        self.levelTraversal()


# Runtime: 40 ms, faster than 71.07 % of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.6 MB, less than 27.42 % of Python3 online submissions for Binary Tree Level Order Traversal.

```

##### max depth of n ary tree

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(child) for child in root.children) + 1


# Runtime: 44 ms, faster than 98.54 % of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 14.5 MB, less than 100.00 % of Python3 online submissions for Maximum Depth of N-ary Tree.

````



