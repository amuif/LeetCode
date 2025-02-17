class Solution:
    def minimumSteps(self, s: str) -> int:
        zero_count = 0  
        swaps = 0  

        for ch in s:
            if ch == '0':
                swaps += zero_count  
            else:
                zero_count += 1  

        return swaps
