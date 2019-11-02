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



