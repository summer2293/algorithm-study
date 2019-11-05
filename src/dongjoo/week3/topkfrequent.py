# import heapq

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = dict()
#         for i in nums:
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1
#         k_freq = []
#         for key,freq in freq.items():
#             heapq.heappush(k_freq, (-freq, key))
#         answer = []
#         for i in range(k):
#             answer.append(heapq.heappop(k_freq)[1])
#         return answer


# 1st attempt:
# Runtime: 124 ms, faster than 46.29 % of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.4 MB, less than 6.25 % of Python3 online submissions for Top K Frequent Elements.


# idea for improvment, use Counter, and use use heap replace instead of heapifying the whole list and popping?
# and heapify O(n) to build instead of inserting one by one?

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
