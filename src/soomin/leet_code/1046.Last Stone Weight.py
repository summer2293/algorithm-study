# 5. python nlog n 보고 분석해본 코드 
# Runtime: 40 ms, faster than 55.44% of Python3 online submissions for Last Stone Weight.???
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-x for x in stones]
        # python 은 0 값이 False
        while(len(q) - 1):
            heapq.heapify(q)
            x, y = heapq.heappop(q), heapq.heappop(q)
            heapq.heappush(q, x - y)        
        return -q[0]

# # 4. heap 공부 후 heapq 모듈로 풀어본 코드 
# Runtime: 32 ms, faster than 95.89% of Python3 online submissions for Last Stone Weight.
# import heapq
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         q = [-x for x in stones]
#         while(True):
#             if len(q) == 0:
#                 return 0
#             if len(q) == 1:
#                 return -heapq.heappop(q)
#             heapq.heapify(q)
#             x, y = -heapq.heappop(q), -heapq.heappop(q)
#             smash = x - y
#             if (smash > 0):
#                 heapq.heappush(q, -smash)
        
# 3 풀리퀘 애들꺼 보고 개선해본 코드
# faster than 83.57% of Python3 online submissions for Last Stone Weight.
# import bisect
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones.sort()
#         while(len(stones) > 1):
#             num = stones.pop() - stones.pop() 
#             if num > 0:
#                 bisect.insort_right(stones,num)

#         if len(stones) == 0:
#             return 0
#         if len(stones) == 1:
#             return stones[0]

# 2 제출코드
# from collections import deque
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         while(len(stones) > 1):
#             stones = deque(sorted(stones))
#             num = stones[-1] - stones[-2]
#             if num > 0:
#                 stones.appendleft(num)
#             stones.pop()
#             stones.pop()            
            
#         if len(stones) == 0:
#             return 0
#         if len(stones) == 1:
#             return stones[0]    



# return output none 이 되는 이유를 모르겠당..
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