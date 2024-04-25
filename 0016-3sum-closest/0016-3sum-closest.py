class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the list to apply the two-pointer approach
        nums.sort()
        n = len(nums)
      
        closest_sum = float('inf')
      
        for i in range(n - 2):  
            left_pointer = i + 1
            right_pointer = n - 1
          
            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
              
                if current_sum == target:
                    return current_sum
              
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
              
                if current_sum > target:
                    right_pointer -= 1  
                else:
                    left_pointer += 1 
        return closest_sum