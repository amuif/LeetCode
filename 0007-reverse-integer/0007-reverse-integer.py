class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if x == 0:
            return 0
        
        if x >  0:

            z =int(str(x)[::-1])
            if z>INT_MAX :
                return 0
            return z

        if x < 0:
            y = abs(x) 
            a = int("-" + str(y)[::-1])
            print(a)
            print(y)
            if a < INT_MIN:
                return 0 
            z = "-" + str(y)[::-1]
            return int(z)
        
        