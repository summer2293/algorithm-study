# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        elif t1 == None and t2:
            return t2
        elif t1 and t2 == None:
            return t1

        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.val = t1.val + t2.val
        return t1


# first attempt:
# Runtime: 80 ms, faster than 96.56 % of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 14.2 MB, less than 20.00 % of Python3 online submissions for Merge Two Binary Trees.
