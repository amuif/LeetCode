class Solution:
    def romanToInt(self, s: str) -> int:
        hashed = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sumi = 0
        i=0
        n = len(s)
        while i < n:
            if i < n-1 and hashed[s[i]] < hashed[s[i+1]]:
                sumi += (hashed[s[i+1]] - hashed[s[i]])
                i+=2

            else:
                sumi += hashed[s[i]]
                i+=1

            
        return sumi