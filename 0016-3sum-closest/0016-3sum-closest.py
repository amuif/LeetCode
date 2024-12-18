class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')  # Initialize with infinity for comparison

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1  # Reset pointers for each `i`

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                # Update closest sum if the current sum is closer to the target
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                # Adjust pointers based on comparison with the target
                if curr_sum < target:
                    l += 1  # Increase the sum by moving `l` to the right
                elif curr_sum > target:
                    r -= 1  # Decrease the sum by moving `r` to the left
                else:
                    return curr_sum  # If exactly equal to the target, return immediately

        return closest_sum
