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