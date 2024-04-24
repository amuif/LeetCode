class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if nums[i] > 0: # no more solutions possible
                break
            if i > 0 and nums[i] == nums[i-1]: # skip duplicate element
                continue
            l = i + 1 # left pointer
            r = len(nums) - 1 # right pointer
            while l < r:
                s = nums[i] + nums[l] + nums[r] # sum of triplet
                if s == 0: # found a solution
                    output.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: # skip duplicate element
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # skip duplicate element
                        r -= 1
                    l += 1 # move both pointers
                    r -= 1
                elif s < 0: # sum is too small, move left pointer
                    l += 1
                else: # sum is too large, move right pointer
                    r -= 1
        return output
