class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        for i in num_set:
            count +=i
        return count
        