# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    # def __eq__(self, obj):
    #     return self.val == obj.val

root = TreeNode(1)
rootle = TreeNode(2)
rootri = TreeNode(2)
root.left = rootle
root.right = rootri
rootlele = TreeNode(3)
rootleri = TreeNode(4)
rootle.left = rootlele
rootle.right = rootleri
rootrile = TreeNode(4)
rootriri = TreeNode(3)
rootri.left = rootrile
rootri.right = rootriri



# 2nd attempt, check level order traversal
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


# 1st solution, recursive strategy comparing grandchildren
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root == None:
#             print("null condiditon")
#             return True
#         # if root.left == None or root.right == None:

#         # check grandchildern
#         if root.left and root.right:
#             if root.left.left and root.left.right and root.right.left and root.right.right:
#                 if root.left.left != root.right.right or root.left.right != root.right.left:
#                     # print(root.left.left,root.right.right)
#                     # print(root.left.right,root.right.left)
#                     print("2nd if if")
#                     return False
#             # elif root.left.
#         elif root.left == None and root.right == None:
#             print("2nd if, elif")
#             return True

#         return self.isSymmetric(root.left) and self.isSymmetric(root.right)

