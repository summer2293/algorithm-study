## sorting

##### k-closest-points-to-origin

```python
import heapq
class Solution:
    def kClosest(self, points, K: int):
        distances = []
        for point in points:
            distances.append(point[0]**2 + point[1]**2)
        for idx in range(len(distances)):
            distances[idx] = (distances[idx], idx)
        heapq.heapify(distances)
        return [points[heapq.heappop(distances)[1]] for i in range(K)]


answer = Solution()
print(answer.kClosest([[3, 3], [5, -1], [-2, 4]], 2))

# 2nd attempt:
# Runtime: 784 ms, faster than 48.41% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.3 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.
```

##### valid-anagram

```python

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

# Runtime: 48 ms, faster than 85.87 % of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.2 MB, less than 6.25 % of Python3 online submissions for Valid Anagram.
# Next challenges:


```


## heap

##### last-stone-weight

```python
# 3rd attempt with heap
import heapq

class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            if y == x:
                continue
            else:
                new_weight = y-x
                heapq.heappush(stones, -1 * new_weight)
        if stones:
            return stones[0] * -1
        return 0
            

# performance:
# Runtime: 36 ms, faster than 83.49% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.

# First Attempt
# Runtime: 44 ms, faster than 14.45 % of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 100.00 % of Python3 online submissions for Last Stone Weight.




```

##### top-k-frequent-elements

```python
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        counter = Counter(nums)
        frequent = [0] * len(counter)
        idx = 0
        for key, freq in counter.items():
            frequent[idx] = (-1 * freq, key)
            idx += 1
        heapq.heapify(frequent)
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(frequent)[1])
        return answer

answer = Solution()

print(answer.topKFrequent([3, 0, 1, 0],1))

# result:.. kinda weird: ran same code twice, got vastly different results
# 1st time: 136 ms which was like 15 %

# second time:
# Runtime: 116 ms, faster than 87.12 % of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.3 MB, less than 6.25 % of Python3 online submissions for Top K Frequent Elements.



````