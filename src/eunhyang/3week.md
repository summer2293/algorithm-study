# 3 weeks

# 정렬
## 973.K Closest Points to Origin
```python
class Solution:
    def __init__(self):
        self._q = []

    def kClosest(self, points, K):
        for point in points:
            heapq.heappush(self._q, (point[0]**2 + point[1]**2, point))

        ans = [heapq.heappop(self._q)[1] for _ in range(K)]
        return ans
```

결과
```
Runtime:## 772 ms
, faster than## 58.09%
ofPython3online submissions forK Closest Points to Origin.
Memory Usage:## 19.3 MB
, less than## 5.80%
ofPython3online submissions forK Closest Points to Origin.
```

## 242.Valid Anagram
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True
```

시간초과 :)

찾아봄
```python
def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)
```
아니 나 왜 생각못했지 d0d 매우 충겨겨겨겨격

# 힙
## 1046.Last Stone Weight
```python
class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) != 1:
            heapq._heapify_max(stones)
            x = heapq._heappop_max(stones)
            y = heapq._heappop_max(stones)
            heapq.heappush(stones, abs(x - y))
            if 0 in stones and stones != [0]:
                stones.remove(0)
        return stones[0]
```

결과
```
Runtime:## 40 ms
, faster than## 55.43%
ofPython3online submissions forLast Stone Weight.
Memory Usage:## 13.9 MB
, less than## 100.00%
ofPython3online submissions forLast Stone Weight.
```

## 347.Top K Frequent Elements
```python
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        q = []
        num_count = Counter(nums)
        for num, count in num_count.items():
            heapq.heappush(q, (-count, num))
        return [heapq.heappop(q)[1] for _ in range(k)]
```

결과
```
Runtime:## 116 ms
, faster than## 87.20%
ofPython3online submissions forTop K Frequent Elements.
Memory Usage:## 18.3 MB
, less than## 6.25%
ofPython3online submissions forTop K Frequent Elements.
```
