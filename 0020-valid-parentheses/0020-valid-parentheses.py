class Solution:
    def isValid(self, s: str) -> bool:
        op={'{':'}','(':')','[':']'}
        stack=[]
        for par in s:
            if par in op.keys():
                stack.append(par)
            else:
                if stack and op[stack[-1]] == par:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False