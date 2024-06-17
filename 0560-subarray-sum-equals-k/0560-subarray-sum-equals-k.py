from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        count = 0
        sum_frequency = {0: 1}
        
        for num in nums:
            cumulative_sum += num
            
            if cumulative_sum - k in sum_frequency:
                count += sum_frequency[cumulative_sum - k]
            
            if cumulative_sum in sum_frequency:
                sum_frequency[cumulative_sum] += 1
            else:
                sum_frequency[cumulative_sum] = 1
        
        return count
