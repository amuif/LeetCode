class Solution:
    def coloredCells(self, n: int) -> int:
        output = 1
        for i in range(n):
            output += i*4

        return output
        