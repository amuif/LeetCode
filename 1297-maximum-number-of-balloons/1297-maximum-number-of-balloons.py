class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counted  = Counter(text)
        counted["o"] //= 2
        counted["l"] //= 2
        return min(counted[char] for char in 'balon')

        
