class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxEnding = nums[0]

        for i in range(1, len(nums)):
        
        # Find the maximum sum ending at index i by either extending 
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
            maxEnding = max(maxEnding + nums[i], nums[i])
        
        # Update res if maximum subarray sum ending at index i > res
            res = max(res, maxEnding)
    
        return res