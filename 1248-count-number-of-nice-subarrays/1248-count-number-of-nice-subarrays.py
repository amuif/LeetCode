class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = right = 0
        ans = 0 # Ans is final Answer
        count = 0 # Count is used for Counting all SubArrays when Condition got Satisified
        odds = 0 # Counts No. of Odds in Current Window

        while right < len(nums):
            if nums[right] % 2 != 0: # Odd
                odds += 1
                count = 0
            
            while odds == k: 
                if nums[left] % 2 == 0: 
                    count += 1
                
                if nums[left] % 2 != 0: 
                    odds -= 1
                    count += 1
                
                left += 1
            
            ans += count

            right += 1
        return ans