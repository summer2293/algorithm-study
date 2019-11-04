# 알고리즘 2주차
# Tree
Binary Tree 리스트로 만드는 법
```python
data = [3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
n = iter(data)
tree = TreeNode(next(n))
fringe = deque([tree])
while True:
    head = fringe.popleft()
    try:
        head.left = TreeNode(next(n))
        fringe.append(head.left)
        head.right = TreeNode(next(n))
        fringe.append(head.right)
    except StopIteration:
        break

```

## **104.Maximum Depth of Binary Tree**
```python
class Solution:
    if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

##  617. Merge Two Binary Trees
```python
if not t1 and not t2: return None
ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
return ans
```

난 왜 이걸 생각 못했지..

# Heap
##  136. Single Number
```python
def singleNumber(self, nums) -> int:
    for i in set(nums):
        try:
            nums.remove(i)
            nums.remove(i)
        except ValueError:
            return i
```


## **1.Two Sum**
```python
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(i, j)
                if nums[i] + nums[j] == target:
                    return [i, j]
```

`- `로 빠르게 푸는 법

```python
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num], i
            d[num] = i
```
