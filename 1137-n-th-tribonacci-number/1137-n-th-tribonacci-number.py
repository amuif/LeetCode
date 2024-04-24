class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 0:
            return 0

        for i in range(2, n):
            temp = a + b + c
            a , b , c = b, c, temp

        return temp