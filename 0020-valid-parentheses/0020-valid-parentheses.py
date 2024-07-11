class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        my_dict = {"(":")","{":"}","[":"]"}
        for i in range(len(s)):
            if s[i] in my_dict.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i]!=my_dict[stack.pop()]:
                    return False
        
        return stack == []
                
        