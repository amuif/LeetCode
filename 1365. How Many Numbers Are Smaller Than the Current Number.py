class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        count =0 
        for i in nums:
            for j in nums:
                if i > j:
                    count +=1
            output.append(count)
            count = 0
        return output
        
