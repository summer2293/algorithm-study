# 3weeks
## 이진 탐색
### 350.Intersection of Two Arrays II
```python
class Solution:

    def intersect(self, nums1, nums2):
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans
```

- 결과
```
Runtime:## 68 ms
, faster than## 25.06%
ofPython3online submissions forIntersection of Two Arrays II.kkkk
Memory Usage:## 12.8 MB
, less than## 100.00%
ofPython3online submissions forIntersection of Two Arrays II.
```

## 287.Find the Duplicate Number
```python
import collections
class Solution:
    def findDuplicate(self, nums):
        for item, count in collections.Counter(nums).items():
            if count > 1:
                return item
```

Counter가 어떻게 구현되어있는지 궁금스
For loop 이랑 if 로 있는지 확인하는식으로 구현하면 timeout 인데!
- 결과 
```
Runtime:## 64 ms
, faster than## 99.37%
ofPython3online submissions forFind the Duplicate Number.
Memory Usage:## 15.9 MB
, less than## 7.14%
ofPython3online submissions forFind the Duplicate Number.
```


## 그리디
### 861.Score After Flipping Matrix
오늘 도저히 머리가 안돌아가서 내일 새벽에 풀어볼게 ㅠㅠ
어떻게 푸는지는 대충 알겠는데 예쁘게 코딩이 안된다이.. ㅠ0ㅠ (아직 답보긴 싫구마유)
```python
```
- 결과
```
```

### 921.Minimum Add to Make Parentheses Valid
```python
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        while '()' in S:
            S = S.replace('()', '')
        return len(S)
```

- 결과
```
Runtime:## 24 ms
, faster than## 99.50%
ofPython3online submissions forMinimum Add to Make Parentheses Valid.
Memory Usage:## 12.7 MB
, less than## 100.00%
ofPython3online submissions forMinimum Add to Make Parentheses Valid.
```
