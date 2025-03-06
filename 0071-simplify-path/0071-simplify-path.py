class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dire = path.split("/")
        for i in dire:
            print(stack)
            if i == '.' or i == '/' or i == '':
                continue
            elif i == '..' :
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)
        