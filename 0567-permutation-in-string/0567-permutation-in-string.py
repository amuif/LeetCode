class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if s1_count == Counter(s2[l:r+ 1]):
                return True
            l += 1
            r += 1

        return False
        