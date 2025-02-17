class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxi = 0
        num_zeroes = 0
               
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeroes += 1
            while num_zeroes > k:
                if nums[l] == 0:
                    num_zeroes -= 1
                l += 1
            maxi = max(maxi,r-l + 1)
        return maxi

        