# class Solution:
#     def kClosest(self, points, K: int):
#         distances = []
#         for point in points:
#             distances.append(point[0]**2 + point[1]**2)
#         answer = sorted(enumerate(distances), key=lambda p:p[1])[:K]
#         return [points[idx[0]] for idx in answer]



    
# answer = Solution()
# print(answer.kClosest([[3, 3], [5, -1], [-2, 4]], 2))


# 1st attempt:
# Runtime: 780 ms, faster than 51.68 % of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.3 MB, less than 5.80 % of Python3 online submissions for K Closest Points to Origin.


# idea for improvement: use quick select?
# or maybe heapify then pop min?
import heapq
class Solution:
    def kClosest(self, points, K: int):
        distances = []
        for point in points:
            distances.append(point[0]**2 + point[1]**2)
        for idx in range(len(distances)):
            distances[idx] = (distances[idx], idx)
        heapq.heapify(distances)
        return [points[heapq.heappop(distances)[1]] for i in range(K)]


answer = Solution()
print(answer.kClosest([[3, 3], [5, -1], [-2, 4]], 2))

# 2nd attempt:
# Runtime: 784 ms, faster than 48.41% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.3 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.