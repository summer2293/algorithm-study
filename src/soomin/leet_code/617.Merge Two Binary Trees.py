# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        