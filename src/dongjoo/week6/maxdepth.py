# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children # form of list


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(child) for child in root.children) + 1


# Runtime: 44 ms, faster than 98.54 % of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 14.5 MB, less than 100.00 % of Python3 online submissions for Maximum Depth of N-ary Tree.
