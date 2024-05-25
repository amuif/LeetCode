class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]* (len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        
        
        total = sum(nums)
        for i in range(len(nums)):
            pre = prefix_sum[i]
            post = total - nums[0] - pre  # Calculate sum of elements after current index
            nums = nums[1:] 
            print(pre)
            print(post)
            print("__")
            if post == pre:
                return i
        return -1
        
        