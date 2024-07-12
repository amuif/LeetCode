class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        output = path.split("/")
       

        for i in output:
            if i == '/':
                stack.pop(i)
            elif i == '..':
                stack.pop(-1)
            elif i == '.':
                continue
            else:
                stack.append(i)
       
        newStack = [x for x  in stack if x!='']
        print(newStack)
        return  "/"+"/".join(newStack)
