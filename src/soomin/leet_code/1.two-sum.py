class Solution(object):
    def twoSum(self, nums, target):
        data = {}
        for i,v in enumerate(nums):
            print(i,v)
            n = target - v
            
            if n in data:
                return[data[n], i]
            else:
                data[v] = i