# heap 
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