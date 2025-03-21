class Solution:
    def splitString(self, s: str) -> bool:
        def split(path,i):
            if i == len(s):
                if len(path) <= 1:
                    return False
                for z in range(1,len(path)):
                    if path[z-1]-1 != path[z]:
                        return False
                return True

            num = 0
            for j in range(i,len(s)):
                num = num * 10 + int(s[j]) 
                if not path or path[-1]  ==  num+1:
                    path.append(num)

                    if split(path,j+1):
                        return True
                    path.pop()
            return False
        
        return split([],0)