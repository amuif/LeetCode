class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(len(nums)-1,1,-1):
            # print(nums[i],nums[i-1],nums[i-2])
            if nums[i] < nums[i-1]+nums[i-2]:
                return sum(nums[i-2:i+1])
        return 0



        