# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low , high = 0 , n
        output =  0

        while low <= high:
            mid =  (high + low)//2
            valid = isBadVersion(mid)
            if valid == False:
                low = mid + 1
            if valid == True:
                output = mid
                high  = mid - 1
                

        return output
        