# 1st attempt


# class Solution:
#     def maxSubArray(self, nums):
#         # use input to save space, for memoization
#         for i in range(1, len(nums)):
#             nums[i] = max(nums[i], nums[i] + nums[i-1])
#         return max(nums)



# result:
# Runtime: 76 ms, faster than 78.17 % of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.8 MB, less than 5.69 % of Python3 online submissions for Maximum Subarray.
# time is fast, but how should i decrease memory?
# improvement: can i increase time by keeping a max pointer?



# 2nd attempt, with max pointer
class Solution:
    def maxSubArray(self, nums):
        # use input to save space, for memoization
        maximum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            maximum = max(nums[i], maximum)
        return maximum

# result: not faster at all....
# Runtime: 76 ms, faster than 78.17 % of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.8 MB, less than 5.69 % of Python3 online submissions for Maximum Subarray.


# afterthought, realized you don't need the whole array,
# maybe decrease memory usage that way?
# but isn't the memory the same? since you can't "delete" the input array?

# below is someone else's answer of my afterthought
# found solution after i had already thought of it, 
# independent thought! Good Job!

# class Solution:
#     # @param A, a list of integers
#     # @return an integer
#     # 6:57
#     def maxSubArray(self, A):
#         if not A:
#             return 0

#         curSum = maxSum = A[0]
#         for num in A[1:]:
#             curSum = max(num, curSum + num)
#             maxSum = max(maxSum, curSum)

#         return maxSum
