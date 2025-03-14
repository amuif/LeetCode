class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = 2 ** n
        if k == length // 2:
            return "1"
        
        if k < length // 2:
            return self.findKthBit(n - 1, k)
        
        result = self.findKthBit(n - 1, n - k)
        if result == "0":
            return "1"
        
        return "0"