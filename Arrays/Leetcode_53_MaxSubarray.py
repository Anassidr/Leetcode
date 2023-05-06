# if we don't go below zero, the subarray we have up until that point will always be kept because it contributes to a bigger sum
# this whole problem is solved by understanding the only moment that matters is when we go below zero 

class Solution:
    def maxSubArray(self, nums: int) -> int:
        maxSub = nums[0]
        curSum = 0 

        for n in nums:
            # if we go below zero, we "delete" the prefix, only what comes forward matters
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)
        return maxSub
    
A = Solution()
print(A.maxSubArray([-4,-3,-4]))