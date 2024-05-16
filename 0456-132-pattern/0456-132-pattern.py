class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack  = []
        if len(nums) <3:
            return False

        mini = nums[0]
        
        for i in nums:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if stack and i > stack[-1][1]:
                return True

            stack.append([i,mini])
            mini = min(mini , i)

        return False
            
            


        