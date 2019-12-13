# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __str__(self):
        return self.val


if __name__ == '__main__':
    # tree5 = Node(5)
    # tree6 = Node(6)
    # tree3 = Node(3, [tree5, tree6])
    # tree2 = Node(2)
    # tree4 = Node(4)
    # root = Node(1, [tree3, tree2, tree4])

    # tree14 = Node(14)
    # tree11 = Node(11, [tree14])
    # tree12 = Node(12)
    # tree13 = Node(13)
    # tree6 = Node(6)
    # tree7 = Node(7, [tree11])
    # tree8 = Node(8, [tree12])
    # tree9 = Node(9, [tree13])
    # tree10 = Node(10)
    # tree2 = Node(2)
    # tree3 = Node(3, [tree6, tree7])
    # tree4 = Node(4, [tree8])
    # tree5 = Node(5, [tree9, tree10])
    # root = Node(1, [tree2, tree3, tree4, tree5])

    t8 = Node(8)
    t7 = Node(7)
    t6 = Node(6, [t7])
    t2 = Node(2, [t6])
    t3 = Node(3, [t8])
    t4 = Node(4)
    t5 = Node(5)
    root = Node(1, [t2, t3, t4, t5])

    q = [i for i in root.children]
    max = 1
    while len(q):
        idx = len(q)
        for _ in range(idx):
            poped = q.pop(0)
            if poped.children is not None:
                for j in poped.children:
                    q.append(j)
        max += 1
    print(max)
```

# https://leetcode.com/problems/symmetric-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isMirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.val == t2.val:
        a = isMirror(t1.right, t2.left)
        b = isMirror(t1.left, t2.right)
        return a and b


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return isMirror(root.left, root.right)
```

# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def traversal(r):
    waiting = [r]
    answer = []
    temp = []
    
    while len(waiting):
        for i in waiting:
            temp.append(i.val)
        answer.append(temp)
        temp = []
        
        length = len(waiting)
        
        for i in range(length):
            if waiting[i].left is not None:
                waiting.append(waiting[i].left)
            if waiting[i].right is not None:
                waiting.append(waiting[i].right)

        for _ in range(length):
            waiting.pop(0)
    return answer

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        else:
            return traversal(root)
```

# https://leetcode.com/problems/course-schedule/submissions/

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        no_enter = [i for i in range(numCourses)]
        topological_sort = []
        cnt_edge = [0 for i in range(numCourses)]

        # 위상 정렬을 구현하기 위해 그래프와 진입 차수가 0인 정점을 찾음
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
            cnt_edge[pair[1]] += 1
            try:
                no_enter.remove(pair[1])
            except:
                pass

        # 위상 정렬 구현하기
        queue = no_enter
        if not len(queue):
            return False

        while len(queue):
            node = queue.pop()
            topological_sort.append(node)
            for i in graph[node]:
                cnt_edge[i] -= 1
            for j in graph[node]:
                if cnt_edge[j] == 0:
                    queue.append(j)

        if len(topological_sort) == numCourses:
            return True
        else:
            return False
```