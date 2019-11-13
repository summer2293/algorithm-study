## Greedy

##### Minimum Add to Make Parentheses Valid

```python
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # decrease counter for ')' and increase for '('
        count = 0
        idx = 0
        answer = 0
        while idx < len(S):
            if S[idx] == ")":
                count -= 1
            elif count>= 0 and S[idx] == "(":
                count += 1
            elif count < 0 and S[idx] == "(":
                answer += abs(count)
                count = 1
            idx += 1
        return answer + abs(count)


                     

answer = Solution()

print(answer.minAddToMakeValid("((("))


# Runtime: 28 ms, faster than 98.99% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Add to Make Parentheses Valid.


```

##### score-after-flipping-matrix

```python
# 861. Score After Flipping Matrix
from typing import List
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # check first column, flipping first column is always better
        # because exponentiation is always 1 bigger than summation for this case

        # take care of first column
        for rowidx in range(len(A)):
            if A[rowidx][0] == 0:
                A[rowidx] = [~elem + 2 for elem in A[rowidx]] #bit shift for two's complement
    
        # take care of rows after that with greedy approach
        colidx = 1
        rowidx = 0
        zeros = 0 # count of zeros in each col
        while colidx < len(A[0]):
            # while loop to count zero in each col
            while rowidx < len(A):
                if A[rowidx][colidx] == 0:
                    zeros += 1
                rowidx += 1

            # print("zeros counted", zeros)
            if zeros > len(A)//2: #check to see if more zeros in row, flip row if so
                tempidx = 0 # temp row idx
                # while loop to flip row
                # print("before flipping", A)
                while tempidx < len(A):
                    A[tempidx][colidx] = ~A[tempidx][colidx] + 2
                    tempidx += 1
                # print("AFTER flipping", A)

            zeros = 0 # reset zeros
            rowidx = 0 # reset rowidx
            colidx += 1 # move one column to right

        answer = 0
        expo = len(A[0])-1 # exponentiation for 2 to sum over A
        for row in A:
            for elem in row:
                answer += elem * (2 ** expo)
                expo -= 1
            expo = len(A[0])-1
        # print(A)
        return answer


answer = Solution()
print(answer.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))


# Runtime: 40 ms, faster than 95.31 % of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 12.9 MB, less than 100.00 % of Python3 online submissions for Score After Flipping Matrix.





```


## binary search

##### intersection-of-two-arrays-ii

```python
from typing import List
# 350. Intersection of Two Arrays II
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_one = Counter(nums1)
        nums_two = Counter(nums2)
        return [elem for elem in (nums_one & nums_two).elements()]


answer = Solution()
print(answer.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

# Runtime: 40 ms, faster than 99.86 % of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 12.8 MB, less than 100.00 % of Python3 online submissions for Intersection of Two Arrays II.
# Next challenges:





```

##### find-the-duplicate-number

```python
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for i in nums:
            if i in check:
                return i
            else:
                check.add(i)


answer = Solution()
print(answer.findDuplicate([1, 3, 4, 2, 2]))

# Runtime: 56 ms, faster than 99.94 % of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.6 MB, less than 7.14 % of Python3 online submissions for Find the Duplicate Number.
# Next challenges:


````



## things to discuss
* cycle detection (https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)
* complexity analysis of 861, score after matrix flipping Time Complexity: O(2^R * R * C)이라고 하는데 2^R * 2^C 아닌가..?
* 861 솔루션 코드 엄청 짧고 간결하넹...




