class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output =[]
        part1 =nums[:n]
        part2 = nums[n:]

        for i,j in zip(part1,part2):
            output+=[i,j]

        return output
