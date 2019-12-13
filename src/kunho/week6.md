## 깊이 우선 탐색 (DFS, Depth First Search)
**[leetcode Depth-first Search 101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)**
```python
# 주어진 Tree가 대칭이면 True 아니면 False를 반환
# Runtime: 20 ms, faster than 99.94% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def mirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            one = self.mirror(left.right, right.left)
            two = self.mirror(left.left, right.right)
        return one and two
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.mirror(root.left, root.right)
```
**[leetcode Depth-first Search 207. Course Schedule](https://leetcode.com/problems/course-schedule/)**
```python
# numCourses만큼 수업을 들을 수 있을 때, 주어진 list prerequisites에는 어떤 수업의 선행 수업들이 담겨있다.
# 모든 수업을 들을 수 있으면 True를 반환, 아니라면 False를 반환
# Runtime: 96 ms, faster than 97.54% of Python3 online submissions for Course Schedule.
# Memory Usage: 15.6 MB, less than 63.27% of Python3 online submissions for Course Schedule.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            def dfs(graph, course, check):
                check[course] = 1
                if course in graph:
                    for suf in graph[course]:
                        if check[suf] == 0:
                            if not dfs(graph, suf, check):
                                return False
                        elif check[suf] == 1:
                            return False
                check[course] = 2
                return True
                            
            if not prerequisites:
                return True
            graph = {}
            check = [0] * numCourses
            
            for node in prerequisites:
                necessary, sufficient = node
                if necessary not in graph:
                    graph[necessary] = set()
                graph[necessary].add(sufficient)
            
            for course in range(numCourses):
                if check[course] == 0:
                    if not dfs(graph, course, check):
                        return False
            return True
```

## 너비 우선 탐색 (BFS, Breadth First Search)

**[leetcode Breadth-first Search 559. Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)**
```python
# 트리의 가장 큰 depth를 찾아 반환.
# Runtime: 40 ms, faster than 99.10% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def check_depth(self, node, depth, max_depth):
        max_depth = max(depth, max_depth)
        for child in node.children:
            if child:
                max_depth = self.check_depth(child, depth + 1, max_depth)
        return max_depth
                    
    def maxDepth(self, root: 'Node') -> int:
        depth, max_depth = 1, 1
        if root:
            return(self.check_depth(root, depth, max_depth))
        else:
            return 0
```

**[leetcode Breadth-first Search 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)**
```python
# 트리의 각 depth에 있는 값들을 묶어서 반환
# Runtime: 24 ms, faster than 99.64% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: 
            return []
        travel_list = [root]
        out_list = [[root.val]]
        while travel_list:
            next = []
            for node in travel_list:
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
            travel_list = next
            out_list.append([node.val for node in next])
        return out_list[:-1]
```