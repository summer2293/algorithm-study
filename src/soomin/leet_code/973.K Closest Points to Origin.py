# 973. K Closest Points to Origin

# 처음 정렬할 생각을 못하고 ㅎ..
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
        
#         dap = []
#         result = list(map(lambda v: v[0] **2 + v[1] **2, points))
        
#         for i in range(K):
#             index = result.index(min(result))
#             dap.append(points[index])
#             del result[index]
#             del points[index]
#         return dap