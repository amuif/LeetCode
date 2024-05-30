class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

            
        l , r = 1 , x

        while l <= r:
            mid = ((l+r) // 2)

            if math.floor(x** (1/2)) == mid : 
                return mid

            if mid < l:
                l = mid

            else:
                r = mid 
        return l


        