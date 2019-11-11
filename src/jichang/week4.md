# LeetCode 287_Find_the_Duplicate_Number

```python
"""
Runtime: 56 ms, faster than 45.71% of Python online submissions for Find the Duplicate Number.
Memory Usage: 13.6 MB, less than 45.24% of Python online submissions for Find the Duplicate Number.
"""


import pytest_watch

nums = [1, 3, 4, 2, 2]
output = 2


def test_simple():
    assert solution(nums) == output

def solution(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            return nums[i]

if __name__ == "__main__":
    solution(nums)
```

# LeetCode 350_Intersection_of_Two_Arrays_II

```python
"""
Runtime: 32 ms, faster than 80.90% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 12 MB, less than 15.38% of Python online submissions for Intersection of Two Arrays II.
"""

import pytest_watch

# nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
# output = [4, 9]
nums1, nums2 = [1, 2, 2, 1], [2, 2]
output = [2, 2]


def test_simple():
    assert solution(nums1, nums2) == output

def solution(nums1, nums2):
    nums1_dict = {}
    answer = []
    for i in nums1:
        try:
            nums1_dict[i] += 1
        except:
            nums1_dict[i] = 1
    for i in nums2:
        try:
            if nums1_dict[i] >= 1:
                nums1_dict[i] -= 1
                answer.append(i)
        except:
            pass
    return answer
```

# 861_Score_After_Flipping_Matrix

```python
"""
Runtime: 28 ms, faster than 41.42% of Python online submissions for Score After Flipping Matrix.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Score After Flipping Matrix.
"""
import pytest_watch

A = [[0, 0, 1, 1],
     [1, 0, 1, 0],
     [1, 1, 0, 0]]

output = 39


def test_simple():
    assert solution(A) == output


def solution(A):
    for row in A:
        if row[0] == 0:
            for idx in range(len(row)):
                row[idx] ^= 1

    for i in range(1, len(A[0])):
        nums_of_zero = 0
        nums_of_one = 0
        for j in range(len(A)):
            if A[j][i] == 0:
                nums_of_zero += 1
            else:
                nums_of_one += 1
        if nums_of_zero > nums_of_one:
            for k in range(len(A)):
                A[k][i] ^= 1
    answer = 0

    for rows in A:
        s = [str(i) for i in rows]
        answer += int("".join(s), 2)
    return answer


if __name__ == "__main__":
    solution(A)
```

# Minimum_Add_to_Make_Parentheses_Valid

```python
"""
Runtime: 24 ms, faster than 24.40% of Python online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 11.8 MB, less than 20.00% of Python online submissions for Minimum Add to Make Parentheses Valid.
"""

import pytest_watch

S = ")()"
output = 1


def test_simple():
    assert solution(S) == output

def solution(S):
    stack = []
    answer = len(S)
    for i in S:
        if i == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
                answer -= 2
        else:
            stack.append(i)
    return answer
```