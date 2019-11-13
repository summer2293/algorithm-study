##  350.Intersection of Two Arrays II
```python
#  Your runtime beats 98.28 % of python3 submissions.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:      
        list = []
        nums1.sort()
        nums2.sort()
        # len 비교
        if len(nums1) > len(nums2):
            s,b = nums2, nums1
        else:
            b,s = nums1, nums2
        
        for i in s:
            if i in b:
                list.append(i)
                b.remove(i)
        
        return list
```


## 287. Find the Duplicate Number

```python
# Runtime: 32 ms, faster than 99.55% of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Score After Flipping Matrix.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        finder = {}
        for i in nums:
            try:
                finder[i] += 1 
                return i
            except:
                finder[i] = 0
```

## 861. Score After Flipping Matrix

```python
# Runtime: 40 ms, faster than 93.29% of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Score After Flipping Matrix.
# Next challenges:
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        if (len(A) == 1):
            return 1
        if (len(A[0]) == 1):
            return len(A)
        
        for i in range(len(A)):
            if(A[i][0] == 0):
                A[i] = list(map(lambda x: 1-x, A[i]))

        sum = 2 ** (len(A[0])-1) * len(A)

        for i in range(1,len(A[0])):
            count = 0
            for j in range(len(A)):
                if (A[j][i] == 1):
                    count += 1
            m =  max(count,len(A)-count)
            sum += 2 ** (len(A[0])-i-1) * m
            
        return sum
```

## 921. Minimum Add to Make Parentheses Valid

```python
# Runtime: 32 ms, faster than 92.22% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Next challenges:
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        while("()" in S):
            S = S.replace("()","")
        return len(S)
```





## 알게된 점

##### python join

```python
print(" ".join(map(str, num_list)))
```

##### python range --
```python
for(i in range(5,0,-1))
# 5
# 4
# 3
# 2
# 1
```

