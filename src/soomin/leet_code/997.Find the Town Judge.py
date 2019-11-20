# 997. Find the Town Judge
# Runtime: 772 ms, faster than 98.77% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 17.3 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
# Next challenges:
# 판사는 아무도 믿지 않기 때문에 , k로 나온사람들은 판사가 아님 -1 처리 
# v 는 투표한 사람. 판사일 확률이 있으므로 +1 해주기
# 같은 표를 받더라도 해당하는 사람이 -1이 되기때문에 max 는 무조건 판사 
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return N
        trusted = [0 for _ in range(N+1)]
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1
        m = max(trusted)
        if m == N-1:
            return trusted.index(m)
        return -1
# ## trash code

# import operator
# from collections import Counter
# class Solution:
#     def findJudge(self, N: int, trust: List[List[int]]) -> int:
#         if N == 1:
#             return 1
#         list = [[0 for i in range(N+1) ] for j in  range(N+1)]
#         people = []
#         counter = {}
#         for i in trust:
#             list[i[0]][i[1]] = i[1]
#             try:     
#                 counter[i[1]] += 1
#             except:
#                 counter[i[1]] = 1
        
#         p = max(counter, key=lambda key: counter[key])
        
#         sum = 0 
#         for i in list[p]:
#             sum+=i
#             if sum >= 1:
#                 return -1
        
#         value = sorted(counter.values())
        
#         if(len(value) > 1 and value[-1] == value[-2]):
#             return -1

#         return p