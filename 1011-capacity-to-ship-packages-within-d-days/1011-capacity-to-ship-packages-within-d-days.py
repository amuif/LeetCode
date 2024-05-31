class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r  = max(weights), sum(weights)
        count = r

        def canShip(x):
            ship , curCap = 1 , x

            for w in weights:
                if curCap - w < 0:
                    ship +=1
                    curCap = x
                curCap -=w

            return ship <= days

        while l <= r:
            mid = (l+r) // 2
            if canShip(mid):
                count = min(count,mid)
                r = mid-1 
            else:
                l = mid +  1
            

        return count