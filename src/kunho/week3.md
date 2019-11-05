## Sort
**[leetcode Sort 973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)**
```python
# 2차원 직교 좌표의 점들이 들어있는 List에서 원점 (0,0)에 가장 가까운 K개의 점을 list 형태로 반환

# Runtime: 748 ms, faster than 75.47% of Python3 online submissions
# Memory Usage: 19.2 MB, less than 5.80% of Python3 online submissions
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for point in points:
            point.append(point[0]**2 + point[1]**2)
        points.sort(key=lambda element : element[2])
        for point in points:
            point.pop(2)
        return (points[:K])
```

**[leetcode Sort 242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)**
```python
# 주어진 문자열 s와 t가 서로의 anagram(어구전철)이면 True를 반환, 아니면 False를 반환

# Runtime: 60ms, faster than 60.11% of Python3 online submissions
# Memory Usage: 14.5 MB, less than 6.25% of Python3 online submissions
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        s_list.sort()
        t_list = list(t)
        t_list.sort()
        if s_list != t_list:
            return False
        return True

# Runtime: 60ms, faster than 60.11% of Python3 online submissions
# Memory Usage: 14.6MB, less than 6.25% of Python3 online submissions
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

## Heap
**[leetcode Heap 1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)**
```python
# 바위의 무게가 담긴 list stones가 있다.
# 매 턴마다 가장 무거운 두 개의 바위를 고르고, 충돌시킨다. 
# 둘의 무게가 같다면 두 바위 모두 사라지고, 다르다면 큰 무게를 가진 바위에서 작은 무게를 가진 바위의 값을 뺀 만큼의 바위가 남게 된다.
# 가장 마지막에 남는 한 개의 바위의 무게를 반환

# Runtime: 32 ms, faster than 95.91% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) == 1:
                return stones[0]
            if len(stones) == 0:
                return 0
            stones.sort(reverse=True)
            if stones is not None:
                y = stones.pop(0)
            if stones is not None:
                x = stones.pop(0)
            if y == x:
                continue
            else:
                stones.append(y-x)

```

**[leetcode Heap 347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)**
```python
# 주어진 list nums에서 가장 많이 중복되는 k개의 원소를 list 형태로 반환

# Runtime: 120 ms, faster than 69.31% of Python3 online submissions
# Memory Usage: 18.6 MB, less than 6.25% of Python3 online submissions
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        return_list = []
        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        sorted_list = sorted(x.items(), key=lambda kv: kv[1], reverse=True)
        for idx in range(k):
            return_list.append(sorted_list[idx][0])
        return return_list
```
