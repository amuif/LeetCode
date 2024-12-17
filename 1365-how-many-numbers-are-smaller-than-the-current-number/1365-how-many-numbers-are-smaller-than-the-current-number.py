class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        output = []
        for i in nums:
            output.append(sorted_list.index(i))
        return output