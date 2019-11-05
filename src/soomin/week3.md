## 973. K Closest Points to Origin


```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 처음 정렬할 생각을 못하고 시간초과해서 솔루션봄! 
        # 신기한게 똑같이 람다 생각했느데 결과는... ㅠㅡㅠ
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
        # Runtime: 720 ms, faster than 95.18% of Python3 online submissions for K Closest Points to Origin.
        # Memory Usage: 19.3 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.


        # 시간초과 코드 
        # result = []
        # sortarr = list(map(lambda v: v[0] **2 + v[1] **2, points))
        
        # for i in range(K):
        #     index = sortarr.index(min(sortarr))
        #     dap.append(points[index])
        #     del sortarr[index]
        #     del points[index]
        
        # return result
```



## 242. Valid Anagram

```python
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            if sorted(s) == sorted(t):
                return True
    # Runtime: 72 ms, faster than 24.30% of Python3 online submissions for Valid Anagram.
    # Memory Usage: 14.5 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
    # Next challenges:
    
    # if 줄이기 더빠름
    class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        return sorted(s) == sorted(t)
    # Runtime: 68 ms, faster than 38.86% of Python3 online submissions for Valid Anagram.
    # Memory Usage: 14.7 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
    
    class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    # 의외로 속도 같음 
    # Runtime: 68 ms, faster than 38.86% of Python3 online submissions for Valid Anagram.
    # Memory Usage: 14.7 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
```



## 1046. Last Stone Weight

```python
from collections import deque
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            stones = deque(sorted(stones))
            num = stones[-1] - stones[-2]
            if num > 0:
                stones.appendleft(num)
            stones.pop()
            stones.pop()            
            
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0] 
# Runtime: 40 ms, faster than 55.43% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.

# 원래 짠 코드. return output none 이 되는 이유를 모르겠당..
# from collections import deque
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
        
#         if len(stones) == 0:
#             return 0
#         if len(stones) == 1:
#             print(stones[0])
#             return stones[0]

#         stones = deque(sorted(stones))
#         num = stones[-1] - stones[-2]
#         if num > 0:
#             stones.appendleft(num)
#         stones.pop()
#         stones.pop()
        
#         self.lastStoneWeight(stones)   
```



## 347. Top K Frequent Elements

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(nums)
        result = []
        counter = {}
        for i in nums:
            try:
                counter[i] += 1
            except:
                counter[i] = 1

        return heapq.nlargest(k, counter.keys(), key=counter.get) 
# 솔루션코드 40% 
# Runtime: 128 ms, faster than 29.25% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.4 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
```