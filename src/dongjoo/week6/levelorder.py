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
