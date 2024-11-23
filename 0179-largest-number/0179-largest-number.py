from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings
        nums_str = list(map(str, nums))
        
        # Custom comparator function
        def compare(x, y):
            # Compare concatenated results
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # They are equal
        
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        result = ''.join(nums_str)
        
        # Handle the case where the result is "0" (e.g., [0, 0])
        return '0' if result[0] == '0' else result
