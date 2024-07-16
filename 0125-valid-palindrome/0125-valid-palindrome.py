class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" " , "")
        output = ''
        for i in range(len(s)):
            if s[i].isalnum():
                output += s[i].lower()
        
     
        return output == output[::-1]  