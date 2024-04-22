class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counted = 0 
        for i in costs:
            coins = coins - i
            if coins <0:
                return counted
            counted +=1
        return counted