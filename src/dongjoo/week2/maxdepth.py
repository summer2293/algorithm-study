# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
    
# small error in first attempt with base case, should have checked root == None before root.left and root.right

        
# Result:
# Runtime: 48 ms, faster than 77.65 % of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.4 MB, less than 5.21 % of Python3 online submissions for Maximum Depth of Binary Tree.
