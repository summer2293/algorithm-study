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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = dict()
        for c in s:
            if c in a:
                a[c] += 1
            else:
                a[c] = 1
        for elem in t:
            if elem in a:
                a[elem] -= 1
                if a[elem] < 0:
                    return False
            else:
                return False
        for value in a.values():
            if value > 0:
                return False
        return True


# Runtime: 52 ms, faster than 78.19 % of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.1 MB, less than 9.38 % of Python3 online submissions for Valid Anagram.
# hmm.. absolutely no difference in memory

```


## heap

##### last-stone-weight

```python
import bisect

class Solution:
    def lastStoneWeight(self, stones) -> int:
        if len(stones) < 2:
            return stones[0]
        stones.sort()
        # print(stones)
        while len(stones) > 1:
            # print(stones)
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                new_weight = stones[-1] - stones[-2]
                stones.pop()
                stones.pop()
                bisect.insort_right(stones,new_weight)
        if stones:
            return stones[0]
        else:
            return 0

        
# First Attempt
# Runtime: 44 ms, faster than 14.45 % of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 100.00 % of Python3 online submissions for Last Stone Weight.




```

##### top-k-frequent-elements

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        k_freq = []
        for key,freq in freq.items():
            heapq.heappush(k_freq, (-freq, key))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(k_freq)[1])
        return answer


# 1st attempt:
# Runtime: 124 ms, faster than 46.29 % of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.4 MB, less than 6.25 % of Python3 online submissions for Top K Frequent Elements.





````