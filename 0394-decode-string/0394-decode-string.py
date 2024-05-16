class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        stack = []
        curr = ""
        
        for i in s :
            if i == "[":
                stack.append(num)
                stack.append(curr)
                num , curr = 0 , ""
            
            elif i == "]":
                prevWord = stack.pop()
                prevNum = stack.pop()
                
                curr  = prevWord + prevNum *  curr
            elif i.isnumeric():
                num = num*10 + int(i)

            else:
                curr += i
        
        return curr