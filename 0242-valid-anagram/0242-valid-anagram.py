from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counted = Counter(s)
        t_counted = Counter(t)
        return s_counted == t_counted