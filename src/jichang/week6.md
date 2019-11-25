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
