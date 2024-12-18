class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cost = 0
        res = 0
        for i in costs:
            cost += i
            print(cost)
            if cost > coins:
                return res
            res += 1

        return res
        