class Solution:
    def isThree(self, n: int) -> bool:
        divisor = 0
        for i in range(n):
            if i / n:
                divisor +=1
        
        if divisor >= 3:
            return True 
        else:
            return False 