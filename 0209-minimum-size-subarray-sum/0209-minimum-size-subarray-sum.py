class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
    
        window = l = 0
      
        for end_index, value in enumerate(nums):
            # Add the current number to the sum of the current subarray
            window += value
            while l < len(nums) and window >= target:
                minLength = min(minLength, end_index - l + 1)
                window -= nums[l]
                l += 1
        return minLength if minLength <= len(nums) else 0