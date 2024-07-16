class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                print(l,r)
                return [l+1,r+1]
            if numbers[l] + numbers[r] > target:
                r-=1
            if numbers[l] + numbers[r] < target:
                print(l,r)
                r+=1
        
        
        