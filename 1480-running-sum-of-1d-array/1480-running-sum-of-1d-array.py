class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumi = 0
        output = []

        for i in range(len(nums)):
            sumi += nums[i]
            output.append(sumi)

        return output

        