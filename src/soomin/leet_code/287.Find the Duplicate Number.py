class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        finder = {}
        for i in nums:
            try:
                finder[i] += 1 
                return i
            except:
                finder[i] = 0
                