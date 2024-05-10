class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        
        # Handle the case where n is negative
        if n < 0:
            n = -n  # Make n positive
            x = 1 / x  # Take the reciprocal of x
        
        # Iterate until n becomes 0
        while n > 0:
            # If n is odd, multiply x with result
            if n % 2!= 0:
                result *= x
            
            # Square x and halve n
            x *= x
            n //= 2
        
        return result