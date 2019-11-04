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