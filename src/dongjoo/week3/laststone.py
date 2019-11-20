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

answer = Solution()
print(answer.lastStoneWeight([2,7,4,1,8,1]))
# import bisect

# class Solution:
#     def lastStoneWeight(self, stones) -> int:
#         if len(stones) < 2:
#             return stones[0]
#         stones.sort()
#         # print(stones)
#         while len(stones) > 1:
#             # print(stones)
#             if stones[-1] == stones[-2]:
#                 stones.pop()
#                 stones.pop()
#             else:
#                 new_weight = stones[-1] - stones[-2]
#                 stones.pop()
#                 stones.pop()
#                 bisect.insort_right(stones,new_weight)
#         if stones:
#             return stones[0]
#         else:
#             return 0

    # def binary_insert(self, lst, elem, start, stop):
    #     if elem > lst[-1]:
    #         lst.append(elem)
    #         return
    #     mid = (stop + stop)//2
    #     if lst[mid]
        
# First Attempt
# Runtime: 44 ms, faster than 14.45 % of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 100.00 % of Python3 online submissions for Last Stone Weight.


# room for improvement: use binary search to find insert position instead of sorting everytime
# changed code on top to reflect the binary feature, some improvement seen

