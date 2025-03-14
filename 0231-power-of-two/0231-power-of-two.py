class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0 :
            return False
        if n == 1:
            return True
        
        return False if n %2 !=0 else self.isPowerOfTwo(n//2)