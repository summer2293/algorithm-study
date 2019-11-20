## Binary Search
**[leetcode Binary Search 350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)**
```python
# 두 list nums1, nums2가 주어지면 교집합 원소들을 list형태로 반환

# Time exceed
class Solution:
    def bSearch(self, input_list, target, output_list):
        low = 0
        high = len(input_list) - 1
        mid = 0
        while low <= high:
            mid = (low+high)//2
            if input_list[mid] == target:
                output_list.append(target)
            elif input_list[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1.sort()
        nums2.sort()
        if len(nums1) <= len(nums2):
            for x in nums1:
                self.bSearch(nums2, x, output)
        else:
            for y in nums2:
                self.bSearch(nums1, y, output)

# Runtime: 104 ms, faster than 5.53% of Python3 online submissions
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
class Solution:            
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1.sort()
        nums2.sort()
        if len(nums1) <= len(nums2):
            for x in nums1:
                for y in nums2:
                    if x == y:
                        output.append(y)
                        nums2.remove(y)
                        break
        else:
            for x in nums2:
                for y in nums1:
                    if x == y:
                        output.append(y)
                        nums1.remove(y)
                        break
        return output

#Runtime: 36 ms, faster than 99.97% of Python3 online submissions
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
class Solution:            
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        large_dict = {}
        large, small = nums1, nums2
        if len(nums1) < len(nums2):
            large, small = nums2, nums1
        for x in large:
            if x not in large_dict:
                large_dict[x] = 1
            else:
                large_dict[x] += 1
        for y in small:
            if y in large_dict:
                if large_dict[y]:
                    output.append(y)
                    large_dict[y] -= 1
        return output
```

**[leetcode Binary Search 287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)**
```python
# 주어진 list nums는 n+1개의 원소가 존재하고, 각 원소는 1~n사이의 값을 가진다.
# nums에서 중복되는 원소를 반환

# Runtime: 60ms, faster than 99.94% of Python3 online submissions
# Memory Usage: 17.5MB, less than 7.14% of Python3 online submissions
import collections

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[0][0]
```

## Greedy
**[leetcode Greedy 861. Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/)**
```python
# 0 또는 1로 채워진 2차원 행렬 A이 주어진다. XOR연산을 통해 A의 아무 행 전체나 열 전체를 바꿀 수 있다.
# XOR연산이 끝난 후, 각 행을 2진수로 나타내었을 때 나올 수 있는 최대값을 반환

# Runtime: 32 ms, faster than 100.00% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        rows = len(A)
        columns = len(A[0])
        total_sum= 0
        
        for row in range(rows):
            if A[row][0] == 0:
                for column in range(columns):
                    A[row][column] = A[row][column] ^ 1
        
        A = [list(x) for x in zip(*A)]
        
        for column in range(columns):
            if sum(A[column]) < rows//2 + 1 :
                for row in range(rows):
                    A[column][row] = A[column][row] ^ 1
            total_sum += sum(A[column]) * 2 **(columns-column-1)
        return total_sum
        
```

**[921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)**
```python
# 주어진 string S는 여는 괄호와 닫는 괄호로 구성되어있다. 아무 위치에 여는 괄호와 닫는 괄호를 넣을 수 있다.
# S의 모든 괄호가 유효하게 되는데 필요한 최소한의 괄호의 개수를 반환 

# Runtime: 28 ms, faster than 98.69% of Python3 online submissions
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        s = []
        if not S:
            return 0
        for i in S:
            if s and s[-1] == "(" and i == ")":
                s.pop(-1)
            else:
                s.append(i)
        return len(s)   
```

