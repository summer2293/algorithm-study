## hashtable

##### two-sum

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
    	if (nums.length == 2)
    		return new int[] {0,1};
    	int[] answer = {0,0};
    	int index = 0;
    	for (int i = index; i < nums.length; i++) {
    		for (int j = i + 1; j < nums.length; j++) {
    			if (nums[i] + nums[j] == target) {
    				answer[0] = i;
    				answer[1] = j;
    				return answer;
    				
    			}
    		}
    		index ++;
    	}
    	return answer;
    }
}
```

##### single number

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for elem in nums:
            answer = answer ^ elem
        return answer


# result: 
# first try
# Runtime: 100 ms, faster than 71.96 % of Python3 online submissions for Single Number.
# Memory Usage: 16.3 MB, less than 6.56 % of Python3 online submissions for Single Number.


```


## Tree

##### merge-two-binary-trees

```python

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        elif t1 == None and t2:
            return t2
        elif t1 and t2 == None:
            return t1

        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.val = t1.val + t2.val
        return t1


```

##### max-depth

```python

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

````