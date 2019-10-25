# Two Sum

```python
import pytest_watch

nums = [2, 7, 11, 15]
target = 9
output = [0, 1]

def test_simple():
    assert solution(nums, target) == output

def solution(nums, target):
    """
    시간 복잡도: O(n^2)
    """
    for idx, value in enumerate(nums):
        if target-value in nums:
            if idx != nums.index(target-value):
                return [idx, nums.index(target-value)]

```

# Signle Number

```python
import pytest_watch

nums = [2, 2, 1]
output = 1


def test_simple():
    assert solution(nums) == output

def solution(nums):
    """
    O(n)
    """
    answer = dict()
    for i in nums:
        try:
            answer.pop(i)
        except:
            answer[i] = 1
    return answer.popitem()[0]

    """
    O(n^2)
    """

    # answer = list()
    # for i in nums:
    #     if i in answer:
    #         answer.remove(i)
    #     else:
    #         answer.append(i)
    # return answer[0]

```

# Merge Two Binary Trees

```python
import pytest_watch
import itertools

t1, t2 = [1, 3, 2, 5], [2, 1, 3, 'null', 4, 'null', 7]
output = [3, 4, 5, 5, 4, 'null', 7]


def test_simple():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    output = TreeNode(3)
    output.left = TreeNode(4)
    output.right = TreeNode(5)
    output.left.left = TreeNode(5)
    output.left.right = TreeNode(4)
    output.right.right = TreeNode(7)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    s = Solution()
    a = s.mergeTrees(tree1, tree2)

    # output = TreeNode(3)
    # output.left = TreeNode(4)
    # output.right = TreeNode(5)
    # output.left.left = TreeNode(5)
    # output.left.right = TreeNode(4)
    # output.right.right = TreeNode(7)

```

# Maximum Depth of Binary Tree

```python
import pytest_watch

input = [1, 2, 'null', 3, 'null', 'null', 'null', 4]
output = 3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def test_simple():
    pass
    # assert solution(input) == output


def maxDepth(root):
    """
    트리의 깊이를 반환하는 함수
    """
    if not root:
        return 0
    return 1+ max(maxDepth(root.left), maxDepth(root.right))


def solution(input):
    pass

if __name__ == "__main__":
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)

    print(maxDepth(root))
```