# Leetcode [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

```python
"""
Runtime: 728 ms, faster than 90.90% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.4 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int):
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:K]
```


# Leetcode [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

```python
"""
Runtime: 88 ms, faster than 5.75% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.3 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s) and ''.join(sorted(t)) == ''.join(sorted(s)):
            return True
        else:
            return False

```
-  sort 와 sorted의 차이
list.sort() : 원본을 직접 정렬 , None을 반환함
sorted(list): 원본에 영향을 끼치지 않음, 정렬한 새로운 문자열 혹은 list를 반환함


# LeetCode [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

```python
"""
Runtime: 36 ms, faster than 83.57% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while  (len(stones)>1):
            stones.sort(reverse=True)
            x = stones.pop(0)
            y = stones.pop(0)
            if(x!=y):
                stones.append(x-y)
        if len(stones) == 0:
            return 0
        return stones[0]
```


# LeetCode [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

```python

# 실패
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        num = Counter(nums)
        num.elements()
        # keys
        keys = list(num.keys())
        return keys[:k]

# 두번째 시도
"""
Runtime: 120 ms, faster than 69.76% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.2 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        return [i[0] for i in Counter(nums).most_common(k)]


```