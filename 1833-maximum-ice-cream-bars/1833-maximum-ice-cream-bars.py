class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        __max = max(costs)

        count = [0]*(__max + 1)

        for i in range(len(costs)):
            count[costs[i]] += 1
        

        counted = 0 
        for i in range(1, 1 + __max):
            __count = min(count[i], coins // i)
            coins -= (i)*__count
            
            if coins < 0:
                return counted
            counted += __count
    
        return counted



 