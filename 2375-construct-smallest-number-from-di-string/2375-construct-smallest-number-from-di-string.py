class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        output = ""
        stack = []

        for i in range(len(pattern)+1):
            stack.append(i+1)
            if  i == len(pattern) or  pattern[i] == "I":
                while stack:
                    output += str(stack.pop())

        return output