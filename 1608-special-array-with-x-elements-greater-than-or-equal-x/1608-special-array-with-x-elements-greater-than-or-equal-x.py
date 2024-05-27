class Solution:
    def specialArray(self, nums: List[int]) -> int:
        

        for i in range(len(nums)+1):
            count=0
            for j in range(len(nums)):
                if i<= nums[j]:
                    count+=1
            print (count)
            print (i)
            if count== i:
                return i
        return -1