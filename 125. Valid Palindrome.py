class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in s.lower():
            if(i.isalnum()):
                t+=i
        if t == t[::-1]:
            return True
        
