## Tree
**[leetcode Tree 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)**
```python
# 주어진 트리의 root에서 가장 큰 depth를 return한다.
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)
        if a > b:
            return a+1
        else:
            return b+1
```

**[leetcode Tree 617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)**
```python
# 주어진 binary tree의 root t1, t2의 같은 위치에 있는 값끼리 더한 tree를 return한다.
# 해당 위치의 값이 t1, t2 중 하나만 존재하는 경우, 존재하는 하나의 값만 남겨둔다.

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t2.right = self.mergeTrees(t1.right, t2.right)
        return t1
```
## Hash
**[leetcode Hash 1. Two Sum](https://leetcode.com/problems/two-sum/)**
```python
# 주어진 list nums에서 두 원소의 합이 target이 되게 하는 두 원소의 index를 list로 return한다.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for key in range(len(nums)):
            if target-nums[key] not in dict:
                dict[nums[key]] = key
            else:
                return [dict[target-nums[key]], key]
```

**[leetcode Hash 136. Single Number](https://leetcode.com/problems/single-number/)**
```python
# 주어진 list nums는 특정 원소만 1개 들어있고, 나머지는 2개씩 들어있다. 1개만 들어있는 특정 원소의 값을 return한다.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i in dict:
                del dict[i]
            else:
                dict[i] = 1
        return list(dict.keys())[0]
```