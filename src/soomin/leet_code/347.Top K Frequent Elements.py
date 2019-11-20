# 4. heap.n largest 로 한 경우
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums) 
        return heapq.nlargest(k, counter.keys(), key=counter.get) 

# 3.  heap 공부 후 // solution 코드 공부 후  - counter most common 으로 return 
# import collections
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         #collection counter.common 으로 풀었을 경우 
#         # Runtime: 112 ms, faster than 96.10% of Python3 online submissions for Top K Frequent Elements.    
#         # Memory Usage: 18.1 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
#         counter = collections.Counter(nums) 
#         return list(map(lambda x: x[0], counter.most_common(k)))# heap 

# 2. submit
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         print(nums)
#         result = []
#         counter = {}
#         for i in nums:
#             try:
#                 counter[i] += 1
#             except:
#                 counter[i] = 1

#         return heapq.nlargest(k, counter.keys(), key=counter.get) 

# trash
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         print(nums)
#         result = []
#         counter = {}
#         for i in nums:
#             try:
#                 counter[i] += 1
#             except:
#                 counter[i] = 1

#         for i in range(k):
#             maxnum = max(counter.keys(), key=(lambda k: counter[k]))
#             result.append(maxnum)
#             del counter[maxnum]
#         return result
#         # print(key_max)
#         return heapq.nlargest(k, counter.keys(), key=counter.get) 