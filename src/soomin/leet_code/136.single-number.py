
# 풀었던 코드들이 다 시간초과 ㅠ__ㅠ 솔루션 봤더니 try, exception 을 써서 그렇게 바꾸니 성공했당
class Solution(object):
    def singleNumber(self, nums):
        tmp = {}
        for i in nums:
            try: 
                del tmp[i]
            except:
                tmp[i] = 0
                
        for i in tmp:
            return i

# first - 시간 초과 
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         tmp = {}
#         for i in nums:
#             if i not in tmp.keys():
#                 tmp[i] = 0
#             else:
#                 del tmp[i]        
#         for i in tmp:
#             return i