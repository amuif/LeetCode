class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomnotecounter = Counter(ransomNote)
        magazinecounter = Counter(magazine)
        keys = magazinecounter.keys()
        for k,v in ransomnotecounter.items():
            if k in keys:
                if not (v==magazinecounter[k] or magazinecounter[k]-v > 0):
                    return False
            else:
                return False
        return True
        