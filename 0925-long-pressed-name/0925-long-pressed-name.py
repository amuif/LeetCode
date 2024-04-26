from collections import Counter
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        count = Counter(name)
        ty_count = Counter(typed)
        if set(name) != set(typed):
            return False
        i = 0
        for char in typed:
            if i < len(name) and char == name[i]:
                i += 1
            elif i > 0 and char == name[i-1]:
                continue
            else:
                return False
        
        return i == len(name)
        