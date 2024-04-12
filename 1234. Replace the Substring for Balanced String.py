class Solution:
    def balancedString(self, s: str) -> int:
        fact,target = {} ,{}
        n = len(s)
        for ch in "QWER":
            target[ch] = n // 4
            fact[ch] = s.count(ch)
        to_change = {k:fact[k] - target[k] for k in "QWER" if fact[k]-target[k]>0}
        if not to_change:
            return 0
        required = len(to_change)
        l,r,formed = 0 ,0, 0
        window = {}
        res = (float("inf") , None,None) 
        while r < n:
            ch = s[r]
            window[ch] = window.get(ch,0) + 1
            if ch in to_change and window[ch]==to_change[ch]:
                formed +=1
            while l <=r and formed == required:
                if r -l + 1 < res[0]:
                    res = (r-l + 1 , l , r)
                char = s[l]
                window[char] -=1
                if char in to_change and window[char] < to_change[char]:
                    formed -=1
                l+=1
            r+=1
        return res[0]
