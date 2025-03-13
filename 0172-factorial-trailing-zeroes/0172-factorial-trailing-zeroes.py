class Solution:
    def trailingZeroes(self, n: int) -> int:

        def recurs(num):
            if num == 0:
                return 1
            output = num * recurs(num-1)
            return output

        final = recurs(n)
        count = 0
        while final % 10 == 0 :
            count +=1
            final //=10

        return count

    
        